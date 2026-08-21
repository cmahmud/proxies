# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 413
- HTTP: 308 alive / 86 gold
- HTTPS: 259 alive / 20 gold
- SOCKS4: 208 alive / 151 gold
- SOCKS5: 260 alive / 156 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29939
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
