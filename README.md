# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 368
- HTTP: 352 alive / 82 gold
- HTTPS: 270 alive / 20 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 240 alive / 149 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29906
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
