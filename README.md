# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 406
- HTTP: 424 alive / 81 gold
- HTTPS: 286 alive / 27 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 261 alive / 148 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29960
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
