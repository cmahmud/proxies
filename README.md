# SyndProxy private pool

## Current pool

- Alive now: 1375
- Gold now: 384
- HTTP: 498 alive / 82 gold
- HTTPS: 342 alive / 13 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 298 alive / 141 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21784
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
