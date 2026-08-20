# SyndProxy private pool

## Current pool

- Alive now: 1332
- Gold now: 592
- HTTP: 484 alive / 197 gold
- HTTPS: 366 alive / 93 gold
- SOCKS4: 238 alive / 146 gold
- SOCKS5: 244 alive / 156 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23562
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
