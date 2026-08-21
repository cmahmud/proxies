# SyndProxy private pool

## Current pool

- Alive now: 1419
- Gold now: 442
- HTTP: 537 alive / 105 gold
- HTTPS: 388 alive / 28 gold
- SOCKS4: 233 alive / 149 gold
- SOCKS5: 261 alive / 160 gold

## Historical pool

- Discovered: 159336
- Ever alive: 30485
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
