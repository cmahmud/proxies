# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 381
- HTTP: 188 alive / 72 gold
- HTTPS: 101 alive / 15 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 219 alive / 155 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25802
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
