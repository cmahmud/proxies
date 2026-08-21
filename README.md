# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 401
- HTTP: 263 alive / 79 gold
- HTTPS: 180 alive / 21 gold
- SOCKS4: 252 alive / 160 gold
- SOCKS5: 235 alive / 141 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29620
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
