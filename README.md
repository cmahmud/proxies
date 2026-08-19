# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 504
- HTTP: 376 alive / 182 gold
- HTTPS: 256 alive / 102 gold
- SOCKS4: 208 alive / 108 gold
- SOCKS5: 185 alive / 112 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19362
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
