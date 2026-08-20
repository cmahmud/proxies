# SyndProxy private pool

## Current pool

- Alive now: 1479
- Gold now: 567
- HTTP: 508 alive / 192 gold
- HTTPS: 371 alive / 96 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 372 alive / 131 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23628
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
