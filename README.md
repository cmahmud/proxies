# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 336
- HTTP: 390 alive / 66 gold
- HTTPS: 273 alive / 17 gold
- SOCKS4: 187 alive / 110 gold
- SOCKS5: 233 alive / 143 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16341
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
