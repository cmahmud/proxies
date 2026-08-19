# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 347
- HTTP: 347 alive / 69 gold
- HTTPS: 264 alive / 18 gold
- SOCKS4: 191 alive / 114 gold
- SOCKS5: 235 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16360
- Ever gold: 513

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
