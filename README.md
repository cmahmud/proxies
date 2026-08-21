# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 405
- HTTP: 303 alive / 95 gold
- HTTPS: 215 alive / 34 gold
- SOCKS4: 213 alive / 145 gold
- SOCKS5: 238 alive / 131 gold

## Historical pool

- Discovered: 160996
- Ever alive: 30948
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
