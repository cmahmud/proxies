# SyndProxy private pool

## Current pool

- Alive now: 1596
- Gold now: 558
- HTTP: 654 alive / 180 gold
- HTTPS: 452 alive / 90 gold
- SOCKS4: 236 alive / 128 gold
- SOCKS5: 254 alive / 160 gold

## Historical pool

- Discovered: 138813
- Ever alive: 23009
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
