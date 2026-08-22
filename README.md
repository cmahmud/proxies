# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 376
- HTTP: 347 alive / 80 gold
- HTTPS: 267 alive / 25 gold
- SOCKS4: 195 alive / 126 gold
- SOCKS5: 222 alive / 145 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32318
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
