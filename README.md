# SyndProxy private pool

## Current pool

- Alive now: 1223
- Gold now: 388
- HTTP: 404 alive / 89 gold
- HTTPS: 286 alive / 16 gold
- SOCKS4: 232 alive / 137 gold
- SOCKS5: 301 alive / 146 gold

## Historical pool

- Discovered: 134541
- Ever alive: 21994
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
