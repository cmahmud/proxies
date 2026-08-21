# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 402
- HTTP: 277 alive / 98 gold
- HTTPS: 218 alive / 25 gold
- SOCKS4: 203 alive / 134 gold
- SOCKS5: 241 alive / 145 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28249
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
