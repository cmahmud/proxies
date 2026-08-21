# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 408
- HTTP: 219 alive / 93 gold
- HTTPS: 131 alive / 23 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 211 alive / 151 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27757
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
