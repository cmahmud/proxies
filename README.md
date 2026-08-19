# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 460
- HTTP: 366 alive / 119 gold
- HTTPS: 277 alive / 73 gold
- SOCKS4: 227 alive / 139 gold
- SOCKS5: 226 alive / 129 gold

## Historical pool

- Discovered: 113538
- Ever alive: 16585
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
