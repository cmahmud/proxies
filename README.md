# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 438
- HTTP: 355 alive / 105 gold
- HTTPS: 238 alive / 28 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 262 alive / 165 gold

## Historical pool

- Discovered: 152944
- Ever alive: 28421
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
