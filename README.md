# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 389
- HTTP: 305 alive / 68 gold
- HTTPS: 213 alive / 14 gold
- SOCKS4: 246 alive / 148 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20427
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
