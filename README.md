# SyndProxy private pool

## Current pool

- Alive now: 1297
- Gold now: 393
- HTTP: 450 alive / 88 gold
- HTTPS: 294 alive / 14 gold
- SOCKS4: 244 alive / 130 gold
- SOCKS5: 309 alive / 161 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21442
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
