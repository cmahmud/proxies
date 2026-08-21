# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 396
- HTTP: 219 alive / 91 gold
- HTTPS: 140 alive / 21 gold
- SOCKS4: 213 alive / 129 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 151688
- Ever alive: 27778
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
