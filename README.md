# SyndProxy private pool

## Current pool

- Alive now: 1417
- Gold now: 437
- HTTP: 537 alive / 95 gold
- HTTPS: 310 alive / 24 gold
- SOCKS4: 244 alive / 150 gold
- SOCKS5: 326 alive / 168 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22431
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
