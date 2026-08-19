# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 347
- HTTP: 361 alive / 69 gold
- HTTPS: 267 alive / 19 gold
- SOCKS4: 182 alive / 114 gold
- SOCKS5: 239 alive / 145 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16365
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
