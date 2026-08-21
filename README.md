# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 379
- HTTP: 286 alive / 70 gold
- HTTPS: 183 alive / 22 gold
- SOCKS4: 205 alive / 139 gold
- SOCKS5: 213 alive / 148 gold

## Historical pool

- Discovered: 157407
- Ever alive: 29679
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
