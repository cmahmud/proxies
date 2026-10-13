# pscaper — validated public proxy pool

Automated read-only proxy exports from **[pscaper](https://github.com/cmahmud/pscaper)**.
The collector runs at **[proxy.syndrid.com](https://proxy.syndrid.com/)**, independently
validates listed proxies, and publishes updates here every 30 minutes via GitHub Actions.

## Latest published counters

| Metric | Count |
| --- | ---: |
| Alive now | 2,142 |
| Gold now | 5 |
| Unique discovered | 264,368 |
| Ever alive | 51,453 |
| Ever Gold | 1,588 |

## Export directories

- [alive/](alive/) — currently verified public proxies; per-protocol and combined lists
- [gold/](gold/) — repeatedly verified, higher-scoring subset
- [historical/](historical/) — cumulative discovered, ever-alive, and ever-Gold lists
- [stats.json](stats.json) — full collector snapshot at the last export
- [Automated publishing](.github/workflows/pscaper-sync.yml) — GitHub Actions publisher

**Public API:** [Read-only alive proxies](https://proxy.syndrid.com/api/v1/proxies?tier=alive&protocol=all&format=json&limit=100).

Lists are snapshots, not guarantees of availability. Public proxies are untrusted.
Never send passwords, session tokens, sensitive data or payments through them.
