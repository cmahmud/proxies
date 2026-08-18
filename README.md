# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 278
- HTTP: 293 alive / 37 gold
- HTTPS: 145 alive / 8 gold
- SOCKS4: 208 alive / 138 gold
- SOCKS5: 162 alive / 95 gold

## Historical pool

- Discovered: 102915
- Ever alive: 13929
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
