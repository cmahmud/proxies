# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 208
- HTTP: 286 alive / 23 gold
- HTTPS: 126 alive / 10 gold
- SOCKS4: 210 alive / 102 gold
- SOCKS5: 215 alive / 73 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8342
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
