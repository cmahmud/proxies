# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 360
- HTTP: 342 alive / 89 gold
- HTTPS: 168 alive / 26 gold
- SOCKS4: 165 alive / 104 gold
- SOCKS5: 247 alive / 141 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32568
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
