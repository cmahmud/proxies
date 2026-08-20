# SyndProxy private pool

## Current pool

- Alive now: 1449
- Gold now: 556
- HTTP: 553 alive / 179 gold
- HTTPS: 433 alive / 90 gold
- SOCKS4: 217 alive / 128 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22996
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
