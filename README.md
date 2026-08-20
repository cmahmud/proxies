# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 362
- HTTP: 199 alive / 69 gold
- HTTPS: 108 alive / 14 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 187 alive / 130 gold

## Historical pool

- Discovered: 145560
- Ever alive: 25472
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
