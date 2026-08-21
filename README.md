# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 432
- HTTP: 377 alive / 114 gold
- HTTPS: 202 alive / 31 gold
- SOCKS4: 247 alive / 147 gold
- SOCKS5: 255 alive / 140 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30795
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
