# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 403
- HTTP: 222 alive / 90 gold
- HTTPS: 130 alive / 22 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 212 alive / 150 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27757
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
