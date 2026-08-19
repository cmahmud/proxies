# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 477
- HTTP: 324 alive / 123 gold
- HTTPS: 245 alive / 72 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 238 alive / 142 gold

## Historical pool

- Discovered: 114238
- Ever alive: 16909
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
