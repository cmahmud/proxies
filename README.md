# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 363
- HTTP: 342 alive / 81 gold
- HTTPS: 252 alive / 21 gold
- SOCKS4: 217 alive / 135 gold
- SOCKS5: 211 alive / 126 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32359
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
