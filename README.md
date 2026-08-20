# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 382
- HTTP: 188 alive / 71 gold
- HTTPS: 107 alive / 15 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 215 alive / 157 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25805
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
