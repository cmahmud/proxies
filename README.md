# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 495
- HTTP: 413 alive / 121 gold
- HTTPS: 226 alive / 73 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 258 alive / 153 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16947
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
