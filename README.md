# SyndProxy private pool

## Current pool

- Alive now: 1275
- Gold now: 432
- HTTP: 461 alive / 106 gold
- HTTPS: 338 alive / 30 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 239 alive / 146 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30514
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
