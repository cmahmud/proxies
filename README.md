# SyndProxy private pool

## Current pool

- Alive now: 1596
- Gold now: 584
- HTTP: 634 alive / 197 gold
- HTTPS: 436 alive / 95 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 289 alive / 151 gold

## Historical pool

- Discovered: 136251
- Ever alive: 22754
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
