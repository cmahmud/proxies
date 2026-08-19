# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 348
- HTTP: 362 alive / 68 gold
- HTTPS: 276 alive / 18 gold
- SOCKS4: 193 alive / 116 gold
- SOCKS5: 233 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16358
- Ever gold: 511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
