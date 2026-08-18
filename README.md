# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 277
- HTTP: 305 alive / 37 gold
- HTTPS: 158 alive / 8 gold
- SOCKS4: 239 alive / 137 gold
- SOCKS5: 170 alive / 95 gold

## Historical pool

- Discovered: 102901
- Ever alive: 13908
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
