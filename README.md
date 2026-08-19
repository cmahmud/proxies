# SyndProxy private pool

## Current pool

- Alive now: 1306
- Gold now: 381
- HTTP: 430 alive / 84 gold
- HTTPS: 293 alive / 20 gold
- SOCKS4: 268 alive / 138 gold
- SOCKS5: 315 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21522
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
