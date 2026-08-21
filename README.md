# SyndProxy private pool

## Current pool

- Alive now: 1239
- Gold now: 461
- HTTP: 442 alive / 107 gold
- HTTPS: 298 alive / 27 gold
- SOCKS4: 215 alive / 161 gold
- SOCKS5: 284 alive / 166 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28575
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
