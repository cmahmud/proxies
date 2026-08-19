# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 377
- HTTP: 308 alive / 74 gold
- HTTPS: 217 alive / 17 gold
- SOCKS4: 213 alive / 125 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15896
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
