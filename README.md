# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 377
- HTTP: 377 alive / 83 gold
- HTTPS: 270 alive / 24 gold
- SOCKS4: 181 alive / 117 gold
- SOCKS5: 234 alive / 153 gold

## Historical pool

- Discovered: 158229
- Ever alive: 29897
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
