# SyndProxy private pool

## Current pool

- Alive now: 553
- Gold now: 220
- HTTP: 156 alive / 35 gold
- HTTPS: 87 alive / 12 gold
- SOCKS4: 151 alive / 100 gold
- SOCKS5: 159 alive / 73 gold

## Historical pool

- Discovered: 82965
- Ever alive: 5062
- Ever gold: 285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
