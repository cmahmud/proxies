# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 340
- HTTP: 396 alive / 66 gold
- HTTPS: 279 alive / 17 gold
- SOCKS4: 195 alive / 114 gold
- SOCKS5: 243 alive / 143 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16346
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
