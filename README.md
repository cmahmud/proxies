# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 397
- HTTP: 347 alive / 79 gold
- HTTPS: 216 alive / 22 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 279 alive / 150 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29542
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
