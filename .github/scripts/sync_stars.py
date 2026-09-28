#!/usr/bin/env python3
"""
sync_stars.py — Awesome Jev Star & Metrics Synchronizer

Batch queries the GitHub GraphQL API to update star counts and identify
archived/dead repositories across README.md and catalog/*.md.

Usage:
    python .github/scripts/sync_stars.py          # Quick sync: README.md and Tier-A (fast, ~2s)
    python .github/scripts/sync_stars.py --all    # Full sync: README.md + all 20 catalog files (7,414 repos)
    python .github/scripts/sync_stars.py --files README.md catalog/01-tier-a.md

Requirements:
    - Standard library only (no pip dependencies).
    - GitHub token via GITHUB_TOKEN env var, or local GitHub CLI (`gh auth token`).
"""

import os
import sys
import re
import json
import argparse
import urllib.request
import urllib.error
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set

GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

RESERVED_PATHS = {
    "features", "topics", "collections", "events", "about",
    "pricing", "security", "contact", "join", "login", "settings",
    "organizations", "explore", "trending", "site", "readme", "pulls", "issues"
}


def get_github_token() -> Optional[str]:
    """Retrieve token from env, or fallback to GitHub CLI (`gh auth token`)."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    
    try:
        proc = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
    except Exception:
        pass
    
    return None


def extract_repo_slugs(text: str) -> Set[Tuple[str, str]]:
    """Extract unique (owner, name) tuples from markdown text."""
    pattern = r"https:\/\/github\.com\/([A-Za-z0-9_.\-]+)\/([A-Za-z0-9_.\-]+)"
    matches = re.findall(pattern, text)
    repos = set()
    for owner, name in matches:
        owner_clean = owner.strip()
        name_clean = name.strip()
        name_clean = re.sub(r"[\/\)\"\'`]+$", "", name_clean)
        if name_clean.endswith(".git"):
            name_clean = name_clean[:-4]
        if owner_clean.lower() in RESERVED_PATHS or not name_clean:
            continue
        repos.add((owner_clean, name_clean))
    return repos


def batch_fetch_repo_metadata(repos: List[Tuple[str, str]], token: str, batch_size: int = 100) -> Dict[Tuple[str, str], dict]:
    """
    Fetch repository metadata using GitHub GraphQL API in batches of 100.
    """
    results: Dict[Tuple[str, str], dict] = {}
    total_batches = (len(repos) + batch_size - 1) // batch_size
    
    for b_idx in range(total_batches):
        batch = repos[b_idx * batch_size:(b_idx + 1) * batch_size]
        query_parts = []
        slug_map = {}
        
        for idx, (owner, name) in enumerate(batch):
            alias = f"r_{idx}"
            slug_map[alias] = (owner, name)
            safe_owner = owner.replace('"', '\\"')
            safe_name = name.replace('"', '\\"')
            query_parts.append(f'  {alias}: repository(owner: "{safe_owner}", name: "{safe_name}") {{ stargazerCount isArchived isFork isPrivate }}')
        
        query = "query {\n" + "\n".join(query_parts) + "\n}"
        payload = json.dumps({"query": query}).encode("utf-8")
        
        req = urllib.request.Request(
            GITHUB_GRAPHQL_ENDPOINT,
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "Awesome-Jev-Metrics-Sync"
            }
        )
        
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            print(f"[!] GraphQL HTTP Error {e.code}: {err_body[:200]}", file=sys.stderr, flush=True)
            continue
        except Exception as e:
            print(f"[!] Request error: {e}", file=sys.stderr, flush=True)
            continue
        
        repo_data = data.get("data") or {}
        for alias, (owner, name) in slug_map.items():
            key = (owner.lower(), name.lower())
            info = repo_data.get(alias)
            if info:
                results[key] = {
                    "stars": info.get("stargazerCount", 0),
                    "archived": info.get("isArchived", False),
                    "private": info.get("isPrivate", False),
                    "found": True
                }
            else:
                results[key] = {"found": False}
        
        print(f"    - Processed batch {b_idx + 1}/{total_batches} ({min((b_idx + 1) * batch_size, len(repos))}/{len(repos)} repos)", flush=True)
                
    return results


def format_star_count(stars: int) -> str:
    """Format star count with thousands separators (e.g. 27,095)."""
    return f"{stars:,}"


def update_markdown_content(content: str, metadata: Dict[Tuple[str, str], dict]) -> Tuple[str, int]:
    """
    Update star counts inside a markdown file.
    """
    updates = 0

    def replace_list_star(m):
        nonlocal updates
        prefix = m.group(1)
        owner = m.group(2).lower()
        name = m.group(3).lower()
        old_stars_str = m.group(4)
        is_bold = m.group(0).count("**") >= 2

        data = metadata.get((owner, name))
        if not data or not data.get("found"):
            return m.group(0)

        new_stars = data["stars"]
        new_formatted = format_star_count(new_stars)

        bold_wrap = "**" if (is_bold or new_stars >= 10000) else ""
        replacement = f"{prefix}({bold_wrap}★{new_formatted}{bold_wrap})"

        if old_stars_str != new_formatted:
            updates += 1
        return replacement

    pattern_list = re.compile(
        r"(\* \[[^\]]+\]\(https:\/\/github\.com\/([A-Za-z0-9_.\-]+)\/([A-Za-z0-9_.\-]+)[^\)]*\)\s+)\(\*{0,2}★([0-9,kK\.]+)\*{0,2}\)"
    )
    content = pattern_list.sub(replace_list_star, content)

    def replace_table_star(m):
        nonlocal updates
        cell_prefix = m.group(1)
        owner = m.group(2).lower()
        name = m.group(3).lower()
        old_stars_str = m.group(4)
        cell_suffix = m.group(5)

        data = metadata.get((owner, name))
        if not data or not data.get("found"):
            return m.group(0)

        new_stars = data["stars"]
        if "," in old_stars_str:
            new_formatted = format_star_count(new_stars)
        else:
            new_formatted = str(new_stars)

        if old_stars_str != new_formatted:
            updates += 1

        return f"{cell_prefix}| {new_formatted} {cell_suffix}"

    pattern_table = re.compile(
        r"(\|\s*\[[^\]]+\]\(https:\/\/github\.com\/([A-Za-z0-9_.\-]+)\/([A-Za-z0-9_.\-]+)[^\)]*\)\s*)\|\s*([0-9,]+)\s*(\|[^\n]*)"
    )
    content = pattern_table.sub(replace_table_star, content)

    return content, updates


def parse_args():
    parser = argparse.ArgumentParser(description="Synchronize star counts and repository health.")
    parser.add_argument("--all", action="store_true", help="Sync all catalog files (7,414 repos) instead of just README and Tier-A.")
    parser.add_argument("--files", nargs="+", help="Specific markdown file paths to sync.")
    return parser.parse_args()


def main():
    args = parse_args()
    token = get_github_token()
    if not token:
        print("[!] No GitHub token found. Please set GITHUB_TOKEN or login via `gh auth login`.", file=sys.stderr, flush=True)
        sys.exit(1)

    target_files = []
    if args.files:
        for f in args.files:
            p = Path(f)
            if not p.is_absolute():
                p = ROOT_DIR / p
            if p.exists():
                target_files.append(p)
    elif args.all:
        readme = ROOT_DIR / "README.md"
        if readme.exists():
            target_files.append(readme)
        catalog_dir = ROOT_DIR / "catalog"
        if catalog_dir.exists():
            target_files.extend(sorted(catalog_dir.glob("*.md")))
    else:
        # Default: Fast sync for primary showcase files
        readme = ROOT_DIR / "README.md"
        if readme.exists():
            target_files.append(readme)
        tier_a = ROOT_DIR / "catalog" / "01-tier-a.md"
        if tier_a.exists():
            target_files.append(tier_a)

    print(f"[*] Target files ({len(target_files)}):", flush=True)
    for tf in target_files:
        print(f"    • {tf.relative_to(ROOT_DIR)}", flush=True)

    all_repos: Set[Tuple[str, str]] = set()
    file_contents = {}

    for path in target_files:
        try:
            text = path.read_text(encoding="utf-8")
            file_contents[path] = text
            repos = extract_repo_slugs(text)
            all_repos.update(repos)
        except Exception as e:
            print(f"[!] Could not read {path.name}: {e}", file=sys.stderr, flush=True)

    repo_list = sorted(list(all_repos))
    print(f"[*] Extracted {len(repo_list)} unique repositories.", flush=True)

    print(f"[*] Querying GitHub GraphQL API...", flush=True)
    metadata = batch_fetch_repo_metadata(repo_list, token, batch_size=100)

    found_count = sum(1 for m in metadata.values() if m.get("found"))
    archived_count = sum(1 for m in metadata.values() if m.get("archived"))
    missing_count = sum(1 for m in metadata.values() if not m.get("found"))
    print(f"[*] API Status: {found_count} active, {archived_count} archived, {missing_count} not found/renamed.", flush=True)

    total_file_updates = 0
    modified_files = []

    for path, content in file_contents.items():
        updated_content, file_updates = update_markdown_content(content, metadata)
        if file_updates > 0:
            path.write_text(updated_content, encoding="utf-8")
            total_file_updates += file_updates
            modified_files.append((path.name, file_updates))

    print(f"\n[+] Synchronization Complete!", flush=True)
    print(f"    - Total metrics updated: {total_file_updates}", flush=True)
    print(f"    - Files modified: {len(modified_files)}", flush=True)
    for fname, count in modified_files:
        print(f"      • {fname}: {count} metric values updated", flush=True)

    if archived_count > 0:
        print(f"\n[!] Archived repositories flagged:", flush=True)
        for (owner, name), data in metadata.items():
            if data.get("archived"):
                print(f"    - {owner}/{name} (Archived on GitHub)", flush=True)


if __name__ == "__main__":
    main()
