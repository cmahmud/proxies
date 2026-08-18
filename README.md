# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 287
- HTTP: 313 alive / 28 gold
- HTTPS: 218 alive / 4 gold
- SOCKS4: 239 alive / 139 gold
- SOCKS5: 250 alive / 116 gold

## Historical pool

- Discovered: 101236
- Ever alive: 12670
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
