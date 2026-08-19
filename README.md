# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 366
- HTTP: 347 alive / 74 gold
- HTTPS: 240 alive / 13 gold
- SOCKS4: 204 alive / 126 gold
- SOCKS5: 225 alive / 153 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20373
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
