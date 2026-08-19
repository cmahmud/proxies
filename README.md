# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 345
- HTTP: 355 alive / 66 gold
- HTTPS: 194 alive / 12 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 200 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20239
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
