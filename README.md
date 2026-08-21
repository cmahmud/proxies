# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 438
- HTTP: 345 alive / 104 gold
- HTTPS: 231 alive / 29 gold
- SOCKS4: 197 alive / 140 gold
- SOCKS5: 256 alive / 165 gold

## Historical pool

- Discovered: 152944
- Ever alive: 28413
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
