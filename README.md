# SyndProxy private pool

## Current pool

- Alive now: 1397
- Gold now: 555
- HTTP: 459 alive / 188 gold
- HTTPS: 347 alive / 90 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 358 alive / 129 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23623
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
