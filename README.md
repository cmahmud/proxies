# SyndProxy private pool

## Current pool

- Alive now: 1287
- Gold now: 381
- HTTP: 422 alive / 85 gold
- HTTPS: 288 alive / 16 gold
- SOCKS4: 251 alive / 139 gold
- SOCKS5: 326 alive / 141 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21473
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
