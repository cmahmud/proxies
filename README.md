# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 428
- HTTP: 391 alive / 124 gold
- HTTPS: 273 alive / 41 gold
- SOCKS4: 218 alive / 124 gold
- SOCKS5: 250 alive / 139 gold

## Historical pool

- Discovered: 117088
- Ever alive: 17133
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
