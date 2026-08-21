# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 403
- HTTP: 218 alive / 90 gold
- HTTPS: 127 alive / 22 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 207 alive / 150 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27757
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
