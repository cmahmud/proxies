# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 492
- HTTP: 382 alive / 119 gold
- HTTPS: 276 alive / 70 gold
- SOCKS4: 225 alive / 155 gold
- SOCKS5: 284 alive / 148 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17040
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
