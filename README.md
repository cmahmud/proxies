# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 513
- HTTP: 374 alive / 153 gold
- HTTPS: 270 alive / 85 gold
- SOCKS4: 190 alive / 134 gold
- SOCKS5: 205 alive / 141 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
