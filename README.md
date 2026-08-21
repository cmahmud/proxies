# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 416
- HTTP: 219 alive / 93 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 216 alive / 160 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27719
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
