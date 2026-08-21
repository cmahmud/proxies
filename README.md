# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 399
- HTTP: 347 alive / 107 gold
- HTTPS: 242 alive / 22 gold
- SOCKS4: 215 alive / 145 gold
- SOCKS5: 223 alive / 125 gold

## Historical pool

- Discovered: 153279
- Ever alive: 28513
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
