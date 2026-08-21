# SyndProxy private pool

## Current pool

- Alive now: 1248
- Gold now: 373
- HTTP: 480 alive / 101 gold
- HTTPS: 291 alive / 24 gold
- SOCKS4: 207 alive / 111 gold
- SOCKS5: 270 alive / 137 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28331
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
