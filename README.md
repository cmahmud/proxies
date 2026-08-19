# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 531
- HTTP: 390 alive / 157 gold
- HTTPS: 242 alive / 84 gold
- SOCKS4: 225 alive / 151 gold
- SOCKS5: 207 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18041
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
