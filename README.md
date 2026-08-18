# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 289
- HTTP: 375 alive / 29 gold
- HTTPS: 165 alive / 6 gold
- SOCKS4: 244 alive / 130 gold
- SOCKS5: 243 alive / 124 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13122
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
