# SyndProxy private pool

## Current pool

- Alive now: 1227
- Gold now: 391
- HTTP: 448 alive / 84 gold
- HTTPS: 248 alive / 15 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 291 alive / 145 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21782
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
