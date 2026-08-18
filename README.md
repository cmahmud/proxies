# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 252
- HTTP: 266 alive / 36 gold
- HTTPS: 127 alive / 9 gold
- SOCKS4: 213 alive / 124 gold
- SOCKS5: 206 alive / 83 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9330
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
