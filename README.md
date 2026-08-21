# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 452
- HTTP: 326 alive / 102 gold
- HTTPS: 237 alive / 30 gold
- SOCKS4: 201 alive / 152 gold
- SOCKS5: 264 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28742
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
