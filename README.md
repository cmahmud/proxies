# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 360
- HTTP: 324 alive / 75 gold
- HTTPS: 213 alive / 18 gold
- SOCKS4: 206 alive / 124 gold
- SOCKS5: 248 alive / 143 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15788
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
