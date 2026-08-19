# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 348
- HTTP: 385 alive / 68 gold
- HTTPS: 274 alive / 18 gold
- SOCKS4: 192 alive / 114 gold
- SOCKS5: 241 alive / 148 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16347
- Ever gold: 511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
