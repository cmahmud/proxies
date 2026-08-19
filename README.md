# SyndProxy private pool

## Current pool

- Alive now: 1314
- Gold now: 415
- HTTP: 461 alive / 82 gold
- HTTPS: 294 alive / 17 gold
- SOCKS4: 286 alive / 151 gold
- SOCKS5: 273 alive / 165 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20637
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
