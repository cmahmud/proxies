# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 383
- HTTP: 395 alive / 102 gold
- HTTPS: 280 alive / 25 gold
- SOCKS4: 194 alive / 117 gold
- SOCKS5: 248 alive / 139 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28285
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
