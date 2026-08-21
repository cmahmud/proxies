# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 383
- HTTP: 357 alive / 101 gold
- HTTPS: 254 alive / 25 gold
- SOCKS4: 204 alive / 117 gold
- SOCKS5: 260 alive / 140 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28289
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
