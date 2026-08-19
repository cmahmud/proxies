# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 504
- HTTP: 416 alive / 121 gold
- HTTPS: 243 alive / 74 gold
- SOCKS4: 230 alive / 151 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16982
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
