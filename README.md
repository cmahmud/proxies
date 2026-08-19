# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 472
- HTTP: 400 alive / 119 gold
- HTTPS: 271 alive / 72 gold
- SOCKS4: 222 alive / 140 gold
- SOCKS5: 218 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16537
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
