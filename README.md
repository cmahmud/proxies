# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 347
- HTTP: 366 alive / 67 gold
- HTTPS: 266 alive / 18 gold
- SOCKS4: 192 alive / 116 gold
- SOCKS5: 229 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16360
- Ever gold: 511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
