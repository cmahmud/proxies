# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 461
- HTTP: 416 alive / 119 gold
- HTTPS: 251 alive / 74 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 213 alive / 129 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16629
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
