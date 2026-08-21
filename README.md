# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 445
- HTTP: 351 alive / 98 gold
- HTTPS: 232 alive / 30 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 265 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28731
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
