# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 382
- HTTP: 363 alive / 95 gold
- HTTPS: 262 alive / 27 gold
- SOCKS4: 204 alive / 118 gold
- SOCKS5: 264 alive / 142 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28083
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
