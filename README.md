# SyndProxy private pool

## Current pool

- Alive now: 1346
- Gold now: 409
- HTTP: 490 alive / 79 gold
- HTTPS: 314 alive / 17 gold
- SOCKS4: 236 alive / 157 gold
- SOCKS5: 306 alive / 156 gold

## Historical pool

- Discovered: 134523
- Ever alive: 21902
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
