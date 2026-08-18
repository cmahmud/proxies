# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 367
- HTTP: 313 alive / 61 gold
- HTTPS: 212 alive / 15 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 232 alive / 140 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15139
- Ever gold: 486

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
