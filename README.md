# SyndProxy private pool

## Current pool

- Alive now: 497
- Gold now: 139
- HTTP: 134 alive / 35 gold
- HTTPS: 76 alive / 10 gold
- SOCKS4: 145 alive / 55 gold
- SOCKS5: 142 alive / 39 gold

## Historical pool

- Discovered: 82958
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
