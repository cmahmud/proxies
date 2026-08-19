# SyndProxy private pool

## Current pool

- Alive now: 1347
- Gold now: 397
- HTTP: 457 alive / 89 gold
- HTTPS: 365 alive / 15 gold
- SOCKS4: 244 alive / 129 gold
- SOCKS5: 281 alive / 164 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21419
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
