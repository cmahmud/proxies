# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 391
- HTTP: 412 alive / 105 gold
- HTTPS: 295 alive / 29 gold
- SOCKS4: 209 alive / 120 gold
- SOCKS5: 285 alive / 137 gold

## Historical pool

- Discovered: 152223
- Ever alive: 27993
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
