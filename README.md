# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 358
- HTTP: 349 alive / 89 gold
- HTTPS: 177 alive / 26 gold
- SOCKS4: 167 alive / 104 gold
- SOCKS5: 240 alive / 139 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32568
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
