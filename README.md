# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 490
- HTTP: 395 alive / 119 gold
- HTTPS: 273 alive / 70 gold
- SOCKS4: 236 alive / 152 gold
- SOCKS5: 285 alive / 149 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17047
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
