# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 330
- HTTP: 290 alive / 61 gold
- HTTPS: 196 alive / 12 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 194 alive / 116 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15197
- Ever gold: 489

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
