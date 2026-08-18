# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 275
- HTTP: 314 alive / 35 gold
- HTTPS: 158 alive / 4 gold
- SOCKS4: 238 alive / 133 gold
- SOCKS5: 215 alive / 103 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11414
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
