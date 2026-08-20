# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 382
- HTTP: 201 alive / 72 gold
- HTTPS: 120 alive / 13 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 218 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25806
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
