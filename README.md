# SyndProxy private pool

## Current pool

- Alive now: 1359
- Gold now: 563
- HTTP: 437 alive / 187 gold
- HTTPS: 333 alive / 99 gold
- SOCKS4: 228 alive / 147 gold
- SOCKS5: 361 alive / 130 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23624
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
