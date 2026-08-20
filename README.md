# SyndProxy private pool

## Current pool

- Alive now: 704
- Gold now: 381
- HTTP: 166 alive / 74 gold
- HTTPS: 125 alive / 19 gold
- SOCKS4: 201 alive / 139 gold
- SOCKS5: 212 alive / 149 gold

## Historical pool

- Discovered: 145562
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
