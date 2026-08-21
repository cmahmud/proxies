# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 389
- HTTP: 392 alive / 102 gold
- HTTPS: 251 alive / 24 gold
- SOCKS4: 217 alive / 124 gold
- SOCKS5: 261 alive / 139 gold

## Historical pool

- Discovered: 152217
- Ever alive: 27967
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
