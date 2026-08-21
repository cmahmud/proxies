# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 396
- HTTP: 320 alive / 89 gold
- HTTPS: 213 alive / 29 gold
- SOCKS4: 246 alive / 146 gold
- SOCKS5: 247 alive / 132 gold

## Historical pool

- Discovered: 160991
- Ever alive: 30895
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
