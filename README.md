# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 209
- HTTP: 365 alive / 23 gold
- HTTPS: 141 alive / 11 gold
- SOCKS4: 214 alive / 102 gold
- SOCKS5: 207 alive / 73 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8338
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
