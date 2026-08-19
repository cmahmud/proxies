# SyndProxy private pool

## Current pool

- Alive now: 1351
- Gold now: 397
- HTTP: 452 alive / 90 gold
- HTTPS: 374 alive / 14 gold
- SOCKS4: 246 alive / 129 gold
- SOCKS5: 279 alive / 164 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21419
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
