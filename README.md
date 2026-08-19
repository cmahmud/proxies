# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 470
- HTTP: 329 alive / 124 gold
- HTTPS: 273 alive / 85 gold
- SOCKS4: 214 alive / 142 gold
- SOCKS5: 188 alive / 119 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17468
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
