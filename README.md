# SyndProxy private pool

## Current pool

- Alive now: 1374
- Gold now: 583
- HTTP: 543 alive / 190 gold
- HTTPS: 347 alive / 96 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 259 alive / 158 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23134
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
