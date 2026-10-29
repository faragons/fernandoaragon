#!/usr/bin/env python3
"""Fetch citation metrics from a Google Scholar profile and save them to _data/scholar.json.

Run daily by .github/workflows/update-scholar.yml. If Google Scholar can't be
reached or the page can't be read, the existing file is left untouched, so the
website keeps showing the last good numbers.
"""
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER_ID = "PqTDOgUAAAAJ"
URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en"
OUT = Path(__file__).resolve().parent.parent / "_data" / "scholar.json"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/129.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def parse(html: str) -> dict:
    """Read the 'Cited by' table: Citations / h-index / i10-index, All and Since YEAR."""
    table = re.search(r'<table[^>]*id="gsc_rsb_st".*?</table>', html, re.S)
    if not table:
        raise ValueError("citation table not found (Scholar may have blocked the request)")
    cells = re.findall(r'class="gsc_rsb_std"[^>]*>\s*([\d,]+)\s*<', table.group(0))
    nums = [int(c.replace(",", "")) for c in cells]
    if len(nums) != 6:
        raise ValueError(f"expected 6 numbers in citation table, found {len(nums)}")
    since = re.search(r"Since\s+(\d{4})", table.group(0))
    return {
        "citations": nums[0],
        "citations_since": nums[1],
        "h_index": nums[2],
        "h_index_since": nums[3],
        "i10_index": nums[4],
        "i10_index_since": nums[5],
        "since_year": int(since.group(1)) if since else None,
    }


def main() -> int:
    last_err = None
    for attempt in range(3):
        try:
            data = parse(fetch(URL))
            break
        except Exception as e:  # network error, block page, layout change
            last_err = e
            time.sleep(10 * (attempt + 1))
    else:
        print(f"::warning::Could not update Google Scholar citations: {last_err}")
        return 0

    data["citations_fmt"] = f"{data['citations']:,}"
    data["citations_since_fmt"] = f"{data['citations_since']:,}"
    data["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    data["profile"] = URL

    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print("Updated citations:", data["citations"], "h-index:", data["h_index"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
