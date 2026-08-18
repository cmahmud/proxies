# SyndProxy private pool

## Current pool

- Alive now: 1159
- Gold now: 285
- HTTP: 475 alive / 30 gold
- HTTPS: 246 alive / 7 gold
- SOCKS4: 214 alive / 127 gold
- SOCKS5: 224 alive / 121 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13108
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
