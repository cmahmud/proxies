# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 391
- HTTP: 309 alive / 93 gold
- HTTPS: 252 alive / 25 gold
- SOCKS4: 237 alive / 134 gold
- SOCKS5: 246 alive / 139 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25109
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
