# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 471
- HTTP: 388 alive / 119 gold
- HTTPS: 282 alive / 72 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 214 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16543
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
