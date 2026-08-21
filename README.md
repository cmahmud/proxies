# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 406
- HTTP: 338 alive / 81 gold
- HTTPS: 240 alive / 25 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 245 alive / 153 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29921
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
