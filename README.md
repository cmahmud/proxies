# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 477
- HTTP: 328 alive / 124 gold
- HTTPS: 246 alive / 71 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 243 alive / 141 gold

## Historical pool

- Discovered: 113910
- Ever alive: 16905
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
