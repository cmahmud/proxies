# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 408
- HTTP: 389 alive / 106 gold
- HTTPS: 279 alive / 24 gold
- SOCKS4: 215 alive / 135 gold
- SOCKS5: 239 alive / 143 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28268
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
