# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 413
- HTTP: 354 alive / 84 gold
- HTTPS: 257 alive / 20 gold
- SOCKS4: 205 alive / 152 gold
- SOCKS5: 261 alive / 157 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29945
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
