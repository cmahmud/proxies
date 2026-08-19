# SyndProxy private pool

## Current pool

- Alive now: 1447
- Gold now: 396
- HTTP: 511 alive / 92 gold
- HTTPS: 351 alive / 20 gold
- SOCKS4: 257 alive / 129 gold
- SOCKS5: 328 alive / 155 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22028
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
