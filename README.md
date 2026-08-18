# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 333
- HTTP: 334 alive / 45 gold
- HTTPS: 184 alive / 11 gold
- SOCKS4: 215 alive / 138 gold
- SOCKS5: 223 alive / 139 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14412
- Ever gold: 459

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
