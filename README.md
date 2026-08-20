# SyndProxy private pool

## Current pool

- Alive now: 1527
- Gold now: 572
- HTTP: 548 alive / 196 gold
- HTTPS: 388 alive / 96 gold
- SOCKS4: 228 alive / 147 gold
- SOCKS5: 363 alive / 133 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23645
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
