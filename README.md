# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 515
- HTTP: 371 alive / 185 gold
- HTTPS: 231 alive / 101 gold
- SOCKS4: 201 alive / 111 gold
- SOCKS5: 196 alive / 118 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19375
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
