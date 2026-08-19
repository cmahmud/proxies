# SyndProxy private pool

## Current pool

- Alive now: 1482
- Gold now: 418
- HTTP: 558 alive / 88 gold
- HTTPS: 377 alive / 17 gold
- SOCKS4: 265 alive / 156 gold
- SOCKS5: 282 alive / 157 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20853
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
