# SyndProxy private pool

## Current pool

- Alive now: 1205
- Gold now: 489
- HTTP: 399 alive / 119 gold
- HTTPS: 284 alive / 70 gold
- SOCKS4: 234 alive / 152 gold
- SOCKS5: 288 alive / 148 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17050
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
