# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 351
- HTTP: 343 alive / 71 gold
- HTTPS: 222 alive / 18 gold
- SOCKS4: 211 alive / 120 gold
- SOCKS5: 250 alive / 142 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15782
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
