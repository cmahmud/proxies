# SyndProxy private pool

## Current pool

- Alive now: 1487
- Gold now: 442
- HTTP: 526 alive / 98 gold
- HTTPS: 373 alive / 27 gold
- SOCKS4: 261 alive / 149 gold
- SOCKS5: 327 alive / 168 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22465
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
