# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 366
- HTTP: 303 alive / 74 gold
- HTTPS: 214 alive / 17 gold
- SOCKS4: 239 alive / 151 gold
- SOCKS5: 215 alive / 124 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15905
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
