# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 287
- HTTP: 303 alive / 28 gold
- HTTPS: 215 alive / 4 gold
- SOCKS4: 238 alive / 139 gold
- SOCKS5: 247 alive / 116 gold

## Historical pool

- Discovered: 101236
- Ever alive: 12670
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
