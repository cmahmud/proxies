# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 366
- HTTP: 376 alive / 101 gold
- HTTPS: 255 alive / 28 gold
- SOCKS4: 202 alive / 112 gold
- SOCKS5: 256 alive / 125 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28296
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
