# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 512
- HTTP: 356 alive / 153 gold
- HTTPS: 267 alive / 86 gold
- SOCKS4: 184 alive / 134 gold
- SOCKS5: 201 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
