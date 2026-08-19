# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 471
- HTTP: 314 alive / 124 gold
- HTTPS: 280 alive / 86 gold
- SOCKS4: 211 alive / 142 gold
- SOCKS5: 186 alive / 119 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17470
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
