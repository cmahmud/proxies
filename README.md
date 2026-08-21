# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 445
- HTTP: 363 alive / 103 gold
- HTTPS: 252 alive / 28 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 266 alive / 165 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28752
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
