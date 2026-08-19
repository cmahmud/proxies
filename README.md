# SyndProxy private pool

## Current pool

- Alive now: 1116
- Gold now: 413
- HTTP: 360 alive / 92 gold
- HTTPS: 260 alive / 19 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 273 alive / 160 gold

## Historical pool

- Discovered: 136192
- Ever alive: 22306
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
