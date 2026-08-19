# SyndProxy private pool

## Current pool

- Alive now: 1394
- Gold now: 404
- HTTP: 476 alive / 89 gold
- HTTPS: 375 alive / 17 gold
- SOCKS4: 234 alive / 151 gold
- SOCKS5: 309 alive / 147 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21808
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
