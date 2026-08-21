# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 391
- HTTP: 388 alive / 84 gold
- HTTPS: 201 alive / 21 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 233 alive / 147 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29743
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
