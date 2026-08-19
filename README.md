# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 341
- HTTP: 314 alive / 63 gold
- HTTPS: 202 alive / 13 gold
- SOCKS4: 208 alive / 139 gold
- SOCKS5: 195 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20219
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
