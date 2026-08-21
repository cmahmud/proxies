# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 408
- HTTP: 343 alive / 103 gold
- HTTPS: 264 alive / 29 gold
- SOCKS4: 189 alive / 124 gold
- SOCKS5: 238 alive / 152 gold

## Historical pool

- Discovered: 152759
- Ever alive: 28357
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
