# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 390
- HTTP: 363 alive / 105 gold
- HTTPS: 251 alive / 27 gold
- SOCKS4: 203 alive / 117 gold
- SOCKS5: 268 alive / 141 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28293
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
