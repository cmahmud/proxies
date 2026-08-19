# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 498
- HTTP: 362 alive / 125 gold
- HTTPS: 209 alive / 73 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 263 alive / 152 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16937
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
