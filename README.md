# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 397
- HTTP: 311 alive / 82 gold
- HTTPS: 180 alive / 20 gold
- SOCKS4: 224 alive / 147 gold
- SOCKS5: 259 alive / 148 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29983
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
