# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 369
- HTTP: 360 alive / 101 gold
- HTTPS: 239 alive / 30 gold
- SOCKS4: 200 alive / 112 gold
- SOCKS5: 255 alive / 126 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28299
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
