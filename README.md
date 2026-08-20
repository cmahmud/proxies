# SyndProxy private pool

## Current pool

- Alive now: 679
- Gold now: 358
- HTTP: 168 alive / 67 gold
- HTTPS: 134 alive / 21 gold
- SOCKS4: 184 alive / 131 gold
- SOCKS5: 193 alive / 139 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25759
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
