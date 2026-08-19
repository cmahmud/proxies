# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 495
- HTTP: 397 alive / 120 gold
- HTTPS: 213 alive / 73 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 255 alive / 154 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16942
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
