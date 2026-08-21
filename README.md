# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 415
- HTTP: 324 alive / 106 gold
- HTTPS: 215 alive / 27 gold
- SOCKS4: 226 alive / 154 gold
- SOCKS5: 227 alive / 128 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30827
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
