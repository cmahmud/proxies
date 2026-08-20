# SyndProxy private pool

## Current pool

- Alive now: 1487
- Gold now: 572
- HTTP: 517 alive / 195 gold
- HTTPS: 379 alive / 96 gold
- SOCKS4: 224 alive / 147 gold
- SOCKS5: 367 alive / 134 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23630
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
