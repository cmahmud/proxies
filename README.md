# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 397
- HTTP: 411 alive / 98 gold
- HTTPS: 285 alive / 27 gold
- SOCKS4: 220 alive / 151 gold
- SOCKS5: 205 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30308
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
