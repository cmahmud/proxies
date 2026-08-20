# SyndProxy private pool

## Current pool

- Alive now: 1493
- Gold now: 432
- HTTP: 559 alive / 121 gold
- HTTPS: 355 alive / 23 gold
- SOCKS4: 248 alive / 132 gold
- SOCKS5: 331 alive / 156 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22681
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
