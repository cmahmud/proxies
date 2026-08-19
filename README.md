# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 348
- HTTP: 370 alive / 68 gold
- HTTPS: 244 alive / 18 gold
- SOCKS4: 190 alive / 114 gold
- SOCKS5: 236 alive / 148 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16347
- Ever gold: 511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
