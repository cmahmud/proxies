#!/usr/bin/env python3
"""Publish current pscaper exports to this repository without VPS GitHub credentials.

Called by GitHub Actions in cmahmud/proxies. Does not delete unrelated files,
preserves append-only historical union, and fails closed on fetch errors.
"""
import json
import os
import pathlib
import re
import subprocess
import tempfile

BASE = pathlib.Path.cwd()
DOMAIN = "https://proxy.syndrid.com"
ORIGIN = "129.213.12.22"
PROTOCOLS = ["all", "http", "https", "socks4", "socks5"]
PATHS = (
    [f"{tier}/{proto}.txt" for tier in ("alive", "gold") for proto in PROTOCOLS]
    + [f"historical/{name}.txt" for name in ("all-discovered", "ever-alive", "ever-gold")]
    + ["stats.json"]
)
PROXY_RE = re.compile(r"^(?:https?|socks[45])://[0-9a-fA-F:.[\]]+:[0-9]{1,5}$")


def fetch(relative: str) -> bytes:
    url = f"{DOMAIN}/pool/{relative}"
    args = ["curl", "--fail", "--silent", "--show-error", "--location",
            "--retry", "2", "--retry-delay", "2", "--connect-timeout", "12",
            "--max-time", "90", "--user-agent", "pscaper-github-publisher/1.0"]
    for connection in ([], ["--connect-to", f"proxy.syndrid.com:443:{ORIGIN}:443"]):
        with tempfile.NamedTemporaryFile() as output:
            res = subprocess.run(args + connection + ["--output", output.name, url],
                                 capture_output=True, text=True, timeout=125)
            if res.returncode == 0:
                return pathlib.Path(output.name).read_bytes()
    raise RuntimeError(f"Unable to fetch {relative} over Cloudflare or origin; last error: {res.stderr[:180]}")


def main() -> None:
    received: dict[str, bytes] = {}
    for path in PATHS:
        received[path] = fetch(path)
        print(f"Fetched {path}: {len(received[path])} bytes")
    stats = json.loads(received["stats.json"])
    assert isinstance(stats.get("total"), int) and stats["total"] > 0, "Invalid total"
    assert isinstance(stats.get("alive"), int) and stats["alive"] >= 0, "Invalid alive"
    hist = received["historical/all-discovered.txt"].decode("utf-8").splitlines()
    assert len(hist) >= 100000, "Historical source unexpectedly small; refusing publish"
    # Keep every previously committed historical record; never lose old state
    # if a fresh VPS snapshot has only a partial history.
    for path in ("historical/all-discovered.txt", "historical/ever-alive.txt", "historical/ever-gold.txt"):
        previous = BASE / path
        existing = previous.read_text().splitlines() if previous.exists() else []
        entries = sorted(set(existing) | set(received[path].decode("utf-8").splitlines()))
        entries = [line.strip() for line in entries if line.strip()]
        received[path] = ("\n".join(entries) + "\n").encode()
    # Ensure we never copy error pages or invalid proxy-list records into GitHub.
    for path, body in received.items():
        if path.endswith(".txt"):
            lines = body.decode("utf-8").splitlines()
            if path.startswith(("alive/", "gold/")):
                # Protocol-specific files contain host:port, combined files contain protocol://host:port.
                if len(lines) and not re.match(r"^(?:https?://|socks[45]://)?[0-9a-fA-F.\[\]:]+:[0-9]{1,5}$", lines[0]):
                    raise ValueError(f"Invalid proxy-line sample in {path}: {lines[0][:70]!r}")
    for path, data in received.items():
        dest = BASE / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.read_bytes() == data:
            continue
        temp = dest.with_suffix(dest.suffix + ".next")
        temp.write_bytes(data)
        os.replace(temp, dest)
        print(f"Updated {path}")
    print(f"Checked {len(PATHS)} export files. Alive at source: {stats['alive']}")


if __name__ == "__main__":
    main()
