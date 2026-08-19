# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 494
- HTTP: 396 alive / 121 gold
- HTTPS: 214 alive / 73 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 256 alive / 152 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16937
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
