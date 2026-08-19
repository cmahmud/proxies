# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 393
- HTTP: 369 alive / 90 gold
- HTTPS: 267 alive / 21 gold
- SOCKS4: 222 alive / 132 gold
- SOCKS5: 303 alive / 150 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22144
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
