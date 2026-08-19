# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 326
- HTTP: 297 alive / 61 gold
- HTTPS: 161 alive / 15 gold
- SOCKS4: 204 alive / 124 gold
- SOCKS5: 242 alive / 126 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20104
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
