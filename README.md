# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 370
- HTTP: 354 alive / 78 gold
- HTTPS: 256 alive / 27 gold
- SOCKS4: 179 alive / 115 gold
- SOCKS5: 241 alive / 150 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29917
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
