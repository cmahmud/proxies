# SyndProxy private pool

## Current pool

- Alive now: 1429
- Gold now: 447
- HTTP: 549 alive / 105 gold
- HTTPS: 371 alive / 28 gold
- SOCKS4: 238 alive / 152 gold
- SOCKS5: 271 alive / 162 gold

## Historical pool

- Discovered: 159336
- Ever alive: 30481
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
