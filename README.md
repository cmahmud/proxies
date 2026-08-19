# SyndProxy private pool

## Current pool

- Alive now: 1351
- Gold now: 414
- HTTP: 489 alive / 86 gold
- HTTPS: 334 alive / 17 gold
- SOCKS4: 261 alive / 156 gold
- SOCKS5: 267 alive / 155 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20809
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
