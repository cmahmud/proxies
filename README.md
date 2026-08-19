# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 396
- HTTP: 311 alive / 73 gold
- HTTPS: 211 alive / 13 gold
- SOCKS4: 258 alive / 151 gold
- SOCKS5: 233 alive / 159 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20496
- Ever gold: 866

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
