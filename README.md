# SyndProxy private pool

## Current pool

- Alive now: 1378
- Gold now: 377
- HTTP: 462 alive / 81 gold
- HTTPS: 309 alive / 16 gold
- SOCKS4: 275 alive / 139 gold
- SOCKS5: 332 alive / 141 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21472
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
