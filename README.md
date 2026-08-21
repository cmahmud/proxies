# SyndProxy private pool

## Current pool

- Alive now: 1160
- Gold now: 390
- HTTP: 412 alive / 102 gold
- HTTPS: 285 alive / 29 gold
- SOCKS4: 185 alive / 107 gold
- SOCKS5: 278 alive / 152 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28331
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
