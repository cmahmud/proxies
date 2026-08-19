# SyndProxy private pool

## Current pool

- Alive now: 1274
- Gold now: 388
- HTTP: 468 alive / 82 gold
- HTTPS: 267 alive / 15 gold
- SOCKS4: 245 alive / 147 gold
- SOCKS5: 294 alive / 144 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21782
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
