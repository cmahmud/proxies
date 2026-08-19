# SyndProxy private pool

## Current pool

- Alive now: 1186
- Gold now: 472
- HTTP: 411 alive / 121 gold
- HTTPS: 294 alive / 75 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 244 alive / 135 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16514
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
