# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 459
- HTTP: 368 alive / 118 gold
- HTTPS: 271 alive / 73 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 219 alive / 129 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16594
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
