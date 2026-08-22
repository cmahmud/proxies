# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 362
- HTTP: 295 alive / 79 gold
- HTTPS: 215 alive / 23 gold
- SOCKS4: 180 alive / 118 gold
- SOCKS5: 222 alive / 142 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32297
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
