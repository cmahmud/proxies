# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 401
- HTTP: 339 alive / 112 gold
- HTTPS: 259 alive / 31 gold
- SOCKS4: 208 alive / 118 gold
- SOCKS5: 298 alive / 140 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28021
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
