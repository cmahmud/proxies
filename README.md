# SyndProxy private pool

## Current pool

- Alive now: 867
- Gold now: 209
- HTTP: 317 alive / 23 gold
- HTTPS: 128 alive / 11 gold
- SOCKS4: 215 alive / 102 gold
- SOCKS5: 207 alive / 73 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8338
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
