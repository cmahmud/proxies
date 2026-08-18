# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 275
- HTTP: 308 alive / 35 gold
- HTTPS: 160 alive / 4 gold
- SOCKS4: 239 alive / 133 gold
- SOCKS5: 217 alive / 103 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11414
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
