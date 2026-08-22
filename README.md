# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 388
- HTTP: 266 alive / 88 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 179 alive / 107 gold
- SOCKS5: 246 alive / 168 gold

## Historical pool

- Discovered: 166622
- Ever alive: 32454
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
