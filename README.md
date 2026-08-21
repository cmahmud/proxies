# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 391
- HTTP: 343 alive / 102 gold
- HTTPS: 268 alive / 30 gold
- SOCKS4: 218 alive / 120 gold
- SOCKS5: 293 alive / 139 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28033
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
