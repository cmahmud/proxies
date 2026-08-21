# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 367
- HTTP: 446 alive / 103 gold
- HTTPS: 295 alive / 26 gold
- SOCKS4: 197 alive / 101 gold
- SOCKS5: 269 alive / 137 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28331
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
