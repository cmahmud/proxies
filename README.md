# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 474
- HTTP: 331 alive / 120 gold
- HTTPS: 236 alive / 72 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 243 alive / 142 gold

## Historical pool

- Discovered: 114270
- Ever alive: 16910
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
