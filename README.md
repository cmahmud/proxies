# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 305
- HTTP: 364 alive / 61 gold
- HTTPS: 260 alive / 19 gold
- SOCKS4: 206 alive / 118 gold
- SOCKS5: 208 alive / 107 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15593
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
