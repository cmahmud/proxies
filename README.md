# SyndProxy private pool

## Current pool

- Alive now: 1223
- Gold now: 459
- HTTP: 453 alive / 103 gold
- HTTPS: 287 alive / 31 gold
- SOCKS4: 215 alive / 153 gold
- SOCKS5: 268 alive / 172 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28729
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
