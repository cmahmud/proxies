# SyndProxy private pool

## Current pool

- Alive now: 1398
- Gold now: 564
- HTTP: 472 alive / 189 gold
- HTTPS: 328 alive / 98 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 369 alive / 131 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23624
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
