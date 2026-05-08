#!/usr/bin/env python3
"""
Climate Radar — Link Validator
Validates all source URLs in index.html and reports broken links.

Usage:
    python3 scripts/validate_links.py
    python3 scripts/validate_links.py --verbose
    python3 scripts/validate_links.py --output report.txt

© 2026 Dr. Naif Alsalem. All rights reserved.
"""

import re
import sys
import time
import argparse
import urllib.request
import urllib.error
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Configuration ────────────────────────────────────────────
TIMEOUT = 10
MAX_WORKERS = 5
HTML_FILE = "index.html"
HEADERS = {
    "User-Agent": "ClimateRadar-LinkValidator/2.1 (Strategic Intelligence Platform)"
}

def extract_links(filepath: str) -> list[dict]:
    """Extract all source links from index.html."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match link: "https://..." patterns in the JS data
    pattern = r'link:"(https://[^"]+)"'
    label_pattern = r'linkLabel:"([^"]+)"'
    title_pattern = r'title:"([^"]+)"'
    
    links = re.findall(pattern, content)
    labels = re.findall(label_pattern, content)
    titles = re.findall(title_pattern, content)
    
    results = []
    for i, link in enumerate(links):
        results.append({
            "id": i + 1,
            "url": link,
            "label": labels[i] if i < len(labels) else "Unknown",
            "title": titles[i] if i < len(titles) else "Unknown",
        })
    return results

def check_url(item: dict, verbose: bool = False) -> dict:
    """Check if a URL is reachable."""
    url = item["url"]
    req = urllib.request.Request(url, headers=HEADERS, method="HEAD")
    
    try:
        start = time.time()
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            elapsed = round((time.time() - start) * 1000)
            return {**item, "status": "OK", "code": response.status, "ms": elapsed}
    except urllib.error.HTTPError as e:
        return {**item, "status": "HTTP_ERROR", "code": e.code, "ms": 0}
    except urllib.error.URLError as e:
        return {**item, "status": "UNREACHABLE", "code": 0, "ms": 0, "reason": str(e.reason)}
    except Exception as e:
        return {**item, "status": "ERROR", "code": 0, "ms": 0, "reason": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Climate Radar Link Validator")
    parser.add_argument("--verbose", action="store_true", help="Show all results including OK")
    parser.add_argument("--output", type=str, help="Write report to file")
    args = parser.parse_args()

    print(f"\n◈ CLIMATE RADAR — Link Validator")
    print(f"  Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Source:   {HTML_FILE}\n")

    try:
        links = extract_links(HTML_FILE)
    except FileNotFoundError:
        print(f"  ERROR: {HTML_FILE} not found. Run from repo root.")
        sys.exit(1)

    print(f"  Found {len(links)} source URLs. Checking...\n")
    
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(check_url, item, args.verbose): item for item in links}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            symbol = "✓" if result["status"] == "OK" else "✗"
            if args.verbose or result["status"] != "OK":
                print(f"  {symbol} [{result['status']:12}] {result['url'][:65]}")

    ok = [r for r in results if r["status"] == "OK"]
    broken = [r for r in results if r["status"] != "OK"]
    
    report_lines = [
        "\n" + "─" * 60,
        f"  SUMMARY: {len(ok)}/{len(results)} links OK",
        f"  Broken:  {len(broken)}",
        "─" * 60,
    ]
    
    if broken:
        report_lines.append("\n  BROKEN LINKS:")
        for r in broken:
            report_lines.append(f"  • [{r['code']}] {r['label']}")
            report_lines.append(f"    {r['url']}")
    
    report = "\n".join(report_lines)
    print(report)
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(f"Climate Radar Link Validation Report\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(report)
        print(f"\n  Report saved to: {args.output}")

if __name__ == "__main__":
    main()
