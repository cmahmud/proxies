# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 446
- HTTP: 348 alive / 101 gold
- HTTPS: 247 alive / 30 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 261 alive / 166 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28751
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
