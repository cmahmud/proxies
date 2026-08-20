# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 396
- HTTP: 305 alive / 98 gold
- HTTPS: 234 alive / 27 gold
- SOCKS4: 248 alive / 133 gold
- SOCKS5: 252 alive / 138 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25103
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
