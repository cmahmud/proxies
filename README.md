# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 431
- HTTP: 471 alive / 92 gold
- HTTPS: 324 alive / 23 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 294 alive / 166 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22390
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
