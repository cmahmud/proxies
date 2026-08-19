# SyndProxy private pool

## Current pool

- Alive now: 1294
- Gold now: 382
- HTTP: 439 alive / 87 gold
- HTTPS: 293 alive / 19 gold
- SOCKS4: 277 alive / 137 gold
- SOCKS5: 285 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21528
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
