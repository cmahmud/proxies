# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 366
- HTTP: 385 alive / 82 gold
- HTTPS: 284 alive / 21 gold
- SOCKS4: 182 alive / 115 gold
- SOCKS5: 224 alive / 148 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29884
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
