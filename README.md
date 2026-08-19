# SyndProxy private pool

## Current pool

- Alive now: 1264
- Gold now: 385
- HTTP: 458 alive / 83 gold
- HTTPS: 274 alive / 12 gold
- SOCKS4: 244 alive / 148 gold
- SOCKS5: 288 alive / 142 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21782
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
