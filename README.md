# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 282
- HTTP: 338 alive / 29 gold
- HTTPS: 245 alive / 6 gold
- SOCKS4: 215 alive / 126 gold
- SOCKS5: 229 alive / 121 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13090
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
