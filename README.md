# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 341
- HTTP: 378 alive / 69 gold
- HTTPS: 274 alive / 17 gold
- SOCKS4: 189 alive / 109 gold
- SOCKS5: 233 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16341
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
