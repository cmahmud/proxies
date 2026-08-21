# SyndProxy private pool

## Current pool

- Alive now: 1250
- Gold now: 386
- HTTP: 476 alive / 103 gold
- HTTPS: 294 alive / 25 gold
- SOCKS4: 201 alive / 107 gold
- SOCKS5: 279 alive / 151 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28331
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
