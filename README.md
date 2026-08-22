# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 379
- HTTP: 392 alive / 90 gold
- HTTPS: 281 alive / 25 gold
- SOCKS4: 162 alive / 102 gold
- SOCKS5: 256 alive / 162 gold

## Historical pool

- Discovered: 166626
- Ever alive: 32460
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
