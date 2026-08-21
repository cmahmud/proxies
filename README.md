# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 377
- HTTP: 374 alive / 83 gold
- HTTPS: 274 alive / 24 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 241 alive / 153 gold

## Historical pool

- Discovered: 158229
- Ever alive: 29897
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
