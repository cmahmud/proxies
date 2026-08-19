# SyndProxy private pool

## Current pool

- Alive now: 1128
- Gold now: 428
- HTTP: 388 alive / 124 gold
- HTTPS: 274 alive / 41 gold
- SOCKS4: 217 alive / 124 gold
- SOCKS5: 249 alive / 139 gold

## Historical pool

- Discovered: 117088
- Ever alive: 17128
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
