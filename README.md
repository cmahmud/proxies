# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 323
- HTTP: 303 alive / 43 gold
- HTTPS: 169 alive / 10 gold
- SOCKS4: 233 alive / 140 gold
- SOCKS5: 222 alive / 130 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14300
- Ever gold: 439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
