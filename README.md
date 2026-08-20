# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 376
- HTTP: 206 alive / 72 gold
- HTTPS: 145 alive / 14 gold
- SOCKS4: 215 alive / 148 gold
- SOCKS5: 213 alive / 142 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26396
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
