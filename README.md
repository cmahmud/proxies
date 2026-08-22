# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 431
- HTTP: 342 alive / 100 gold
- HTTPS: 201 alive / 29 gold
- SOCKS4: 233 alive / 144 gold
- SOCKS5: 267 alive / 158 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32549
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
