# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 375
- HTTP: 326 alive / 81 gold
- HTTPS: 244 alive / 27 gold
- SOCKS4: 175 alive / 117 gold
- SOCKS5: 238 alive / 150 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29919
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
