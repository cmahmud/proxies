# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 335
- HTTP: 315 alive / 57 gold
- HTTPS: 201 alive / 13 gold
- SOCKS4: 214 alive / 133 gold
- SOCKS5: 195 alive / 132 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20037
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
