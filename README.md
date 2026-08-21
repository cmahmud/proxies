# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 432
- HTTP: 373 alive / 108 gold
- HTTPS: 263 alive / 30 gold
- SOCKS4: 214 alive / 137 gold
- SOCKS5: 242 alive / 157 gold

## Historical pool

- Discovered: 152762
- Ever alive: 28386
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
