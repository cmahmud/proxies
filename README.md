# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 293
- HTTP: 285 alive / 26 gold
- HTTPS: 178 alive / 4 gold
- SOCKS4: 211 alive / 142 gold
- SOCKS5: 218 alive / 121 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13477
- Ever gold: 416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
