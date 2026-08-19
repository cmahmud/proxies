# SyndProxy private pool

## Current pool

- Alive now: 1178
- Gold now: 379
- HTTP: 384 alive / 93 gold
- HTTPS: 261 alive / 12 gold
- SOCKS4: 239 alive / 139 gold
- SOCKS5: 294 alive / 135 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21022
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
