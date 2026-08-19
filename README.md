# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 382
- HTTP: 447 alive / 85 gold
- HTTPS: 291 alive / 20 gold
- SOCKS4: 270 alive / 138 gold
- SOCKS5: 310 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21519
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
