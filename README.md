# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 473
- HTTP: 297 alive / 120 gold
- HTTPS: 213 alive / 86 gold
- SOCKS4: 178 alive / 129 gold
- SOCKS5: 215 alive / 138 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17516
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
