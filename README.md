# SyndProxy private pool

## Current pool

- Alive now: 1418
- Gold now: 405
- HTTP: 504 alive / 78 gold
- HTTPS: 359 alive / 16 gold
- SOCKS4: 246 alive / 156 gold
- SOCKS5: 309 alive / 155 gold

## Historical pool

- Discovered: 134523
- Ever alive: 21939
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
