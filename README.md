# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 309
- HTTP: 284 alive / 26 gold
- HTTPS: 161 alive / 4 gold
- SOCKS4: 242 alive / 148 gold
- SOCKS5: 236 alive / 131 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12774
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
