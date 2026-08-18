# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 313
- HTTP: 293 alive / 40 gold
- HTTPS: 191 alive / 9 gold
- SOCKS4: 237 alive / 134 gold
- SOCKS5: 218 alive / 130 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14268
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
