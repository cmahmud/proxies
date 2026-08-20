# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 388
- HTTP: 210 alive / 79 gold
- HTTPS: 247 alive / 20 gold
- SOCKS4: 217 alive / 150 gold
- SOCKS5: 231 alive / 139 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26884
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
