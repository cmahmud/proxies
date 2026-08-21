# SyndProxy private pool

## Current pool

- Alive now: 1125
- Gold now: 407
- HTTP: 400 alive / 104 gold
- HTTPS: 291 alive / 29 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28363
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
