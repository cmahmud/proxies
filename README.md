# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 369
- HTTP: 341 alive / 102 gold
- HTTPS: 232 alive / 31 gold
- SOCKS4: 204 alive / 111 gold
- SOCKS5: 256 alive / 125 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28303
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
