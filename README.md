# SyndProxy private pool

## Current pool

- Alive now: 1383
- Gold now: 431
- HTTP: 523 alive / 110 gold
- HTTPS: 319 alive / 24 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 316 alive / 156 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22659
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
