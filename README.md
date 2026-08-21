# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 448
- HTTP: 366 alive / 100 gold
- HTTPS: 241 alive / 31 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 265 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28736
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
