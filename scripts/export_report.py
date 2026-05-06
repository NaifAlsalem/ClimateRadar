#!/usr/bin/env python3
"""
Climate Radar — Report Export Utility
Generates a structured text summary of all signals for offline use or
integration into briefing documents.

Usage:
    python3 scripts/export_report.py
    python3 scripts/export_report.py --risk High
    python3 scripts/export_report.py --category Negotiation --days 30
    python3 scripts/export_report.py --format markdown --output brief.md
"""

import re
import json
import argparse
from datetime import datetime, timedelta

HTML_FILE = "index.html"

RISK_ORDER = {"High": 0, "Medium": 1, "Low": 2}

def extract_signals(filepath: str) -> list[dict]:
    """Parse signal data from index.html JS source."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    signal_pattern = re.compile(
        r'\{id:(\d+),title:"([^"]+)",source:"([^"]+)",risk:"([^"]+)",'
        r'category:"([^"]+)",date:[^,]+,\s*summary:"([^"]+)"',
        re.DOTALL
    )
    
    signals = []
    for m in signal_pattern.finditer(content):
        signals.append({
            "id": int(m.group(1)),
            "title": m.group(2),
            "source": m.group(3),
            "risk": m.group(4),
            "category": m.group(5),
            "summary": m.group(6),
            "date": (datetime.now() - timedelta(days=int(m.group(1)))).strftime("%Y-%m-%d")
        })
    
    return sorted(signals, key=lambda x: RISK_ORDER.get(x["risk"], 3))

def format_text(signals: list[dict]) -> str:
    lines = [
        "CLIMATE RADAR — STRATEGIC INTELLIGENCE BRIEF",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} GST",
        f"Prepared by: Naif Alsalem",
        f"Classification: CONFIDENTIAL",
        "=" * 60,
        f"Total Signals: {len(signals)}",
        f"  High:   {sum(1 for s in signals if s['risk']=='High')}",
        f"  Medium: {sum(1 for s in signals if s['risk']=='Medium')}",
        f"  Low:    {sum(1 for s in signals if s['risk']=='Low')}",
        "=" * 60, ""
    ]
    for s in signals:
        lines += [
            f"[{s['risk'].upper():6}] {s['title']}",
            f"Source: {s['source']}  |  Category: {s['category']}  |  Date: {s['date']}",
            f"{s['summary']}",
            "-" * 60, ""
        ]
    return "\n".join(lines)

def format_markdown(signals: list[dict]) -> str:
    lines = [
        "# Climate Radar — Strategic Intelligence Brief",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')} GST  ",
        f"**Prepared by:** Naif Alsalem  ",
        f"**Classification:** CONFIDENTIAL",
        "",
        "---",
        "",
        f"**Total Signals:** {len(signals)} &nbsp;&nbsp; "
        f"🔴 High: {sum(1 for s in signals if s['risk']=='High')} &nbsp;&nbsp; "
        f"🟡 Medium: {sum(1 for s in signals if s['risk']=='Medium')} &nbsp;&nbsp; "
        f"🟢 Low: {sum(1 for s in signals if s['risk']=='Low')}",
        "", "---", ""
    ]
    for s in signals:
        badge = "🔴" if s["risk"]=="High" else "🟡" if s["risk"]=="Medium" else "🟢"
        lines += [
            f"## {badge} {s['title']}",
            f"**Source:** {s['source']} &nbsp;|&nbsp; **Category:** {s['category']} &nbsp;|&nbsp; **Date:** {s['date']}",
            "",
            s["summary"],
            "", "---", ""
        ]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Climate Radar Report Exporter")
    parser.add_argument("--risk", choices=["High","Medium","Low"], help="Filter by risk level")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--days", type=int, help="Only signals within last N days")
    parser.add_argument("--format", choices=["text","markdown","json"], default="text")
    parser.add_argument("--output", type=str, help="Output file path")
    args = parser.parse_args()

    signals = extract_signals(HTML_FILE)
    
    if args.risk:
        signals = [s for s in signals if s["risk"] == args.risk]
    if args.category:
        signals = [s for s in signals if s["category"].lower() == args.category.lower()]
    
    print(f"\n◈ Climate Radar Export — {len(signals)} signals\n")
    
    if args.format == "json":
        output = json.dumps(signals, indent=2, ensure_ascii=False)
    elif args.format == "markdown":
        output = format_markdown(signals)
    else:
        output = format_text(signals)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"  Saved to: {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()
