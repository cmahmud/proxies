# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 513
- HTTP: 356 alive / 154 gold
- HTTPS: 271 alive / 86 gold
- SOCKS4: 196 alive / 134 gold
- SOCKS5: 204 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
