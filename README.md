# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 367
- HTTP: 353 alive / 80 gold
- HTTPS: 269 alive / 21 gold
- SOCKS4: 182 alive / 117 gold
- SOCKS5: 239 alive / 149 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29908
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
