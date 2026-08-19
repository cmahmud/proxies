# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 352
- HTTP: 366 alive / 71 gold
- HTTPS: 217 alive / 17 gold
- SOCKS4: 204 alive / 120 gold
- SOCKS5: 239 alive / 144 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15771
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
