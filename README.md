# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 278
- HTTP: 312 alive / 36 gold
- HTTPS: 155 alive / 4 gold
- SOCKS4: 232 alive / 133 gold
- SOCKS5: 214 alive / 105 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11414
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
