# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 347
- HTTP: 377 alive / 68 gold
- HTTPS: 278 alive / 18 gold
- SOCKS4: 187 alive / 115 gold
- SOCKS5: 237 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16358
- Ever gold: 511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
