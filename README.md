# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 385
- HTTP: 421 alive / 103 gold
- HTTPS: 297 alive / 25 gold
- SOCKS4: 191 alive / 107 gold
- SOCKS5: 281 alive / 150 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28331
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
