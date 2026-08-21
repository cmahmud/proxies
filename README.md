# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 377
- HTTP: 292 alive / 70 gold
- HTTPS: 169 alive / 21 gold
- SOCKS4: 201 alive / 139 gold
- SOCKS5: 211 alive / 147 gold

## Historical pool

- Discovered: 157407
- Ever alive: 29678
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
