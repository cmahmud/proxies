# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 401
- HTTP: 345 alive / 103 gold
- HTTPS: 265 alive / 27 gold
- SOCKS4: 193 alive / 119 gold
- SOCKS5: 260 alive / 152 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28340
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
