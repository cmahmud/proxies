# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 475
- HTTP: 377 alive / 120 gold
- HTTPS: 222 alive / 72 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 260 alive / 142 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16888
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
