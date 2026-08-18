# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 273
- HTTP: 285 alive / 34 gold
- HTTPS: 190 alive / 4 gold
- SOCKS4: 239 alive / 131 gold
- SOCKS5: 218 alive / 104 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
