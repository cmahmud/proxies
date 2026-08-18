# SyndProxy private pool

## Current pool

- Alive now: 1203
- Gold now: 218
- HTTP: 525 alive / 36 gold
- HTTPS: 231 alive / 10 gold
- SOCKS4: 236 alive / 101 gold
- SOCKS5: 211 alive / 71 gold

## Historical pool

- Discovered: 85839
- Ever alive: 5721
- Ever gold: 287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
