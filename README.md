# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 206
- HTTP: 215 alive / 26 gold
- HTTPS: 107 alive / 9 gold
- SOCKS4: 212 alive / 100 gold
- SOCKS5: 219 alive / 71 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8342
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
