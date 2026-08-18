# SyndProxy private pool

## Current pool

- Alive now: 584
- Gold now: 211
- HTTP: 139 alive / 25 gold
- HTTPS: 85 alive / 7 gold
- SOCKS4: 180 alive / 109 gold
- SOCKS5: 180 alive / 70 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8360
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
