# SyndProxy private pool

## Current pool

- Alive now: 1408
- Gold now: 449
- HTTP: 517 alive / 106 gold
- HTTPS: 374 alive / 34 gold
- SOCKS4: 233 alive / 141 gold
- SOCKS5: 284 alive / 168 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30355
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
