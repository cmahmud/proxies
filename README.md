# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 206
- HTTP: 371 alive / 22 gold
- HTTPS: 142 alive / 11 gold
- SOCKS4: 224 alive / 101 gold
- SOCKS5: 201 alive / 72 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8338
- Ever gold: 348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
