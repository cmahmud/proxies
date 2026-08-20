# SyndProxy private pool

## Current pool

- Alive now: 1436
- Gold now: 568
- HTTP: 497 alive / 192 gold
- HTTPS: 359 alive / 97 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 364 alive / 131 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23628
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
