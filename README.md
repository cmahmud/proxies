# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 331
- HTTP: 269 alive / 62 gold
- HTTPS: 188 alive / 12 gold
- SOCKS4: 221 alive / 141 gold
- SOCKS5: 192 alive / 116 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15200
- Ever gold: 489

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
