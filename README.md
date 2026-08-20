# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 388
- HTTP: 202 alive / 80 gold
- HTTPS: 132 alive / 24 gold
- SOCKS4: 195 alive / 136 gold
- SOCKS5: 238 alive / 148 gold

## Historical pool

- Discovered: 147687
- Ever alive: 25956
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
