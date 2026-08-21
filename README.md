# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 405
- HTTP: 291 alive / 95 gold
- HTTPS: 219 alive / 37 gold
- SOCKS4: 224 alive / 142 gold
- SOCKS5: 260 alive / 131 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30925
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
