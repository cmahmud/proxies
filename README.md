# SyndProxy private pool

## Current pool

- Alive now: 1556
- Gold now: 553
- HTTP: 627 alive / 179 gold
- HTTPS: 448 alive / 90 gold
- SOCKS4: 235 alive / 127 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23030
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
