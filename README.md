# SyndProxy private pool

## Current pool

- Alive now: 1594
- Gold now: 605
- HTTP: 560 alive / 207 gold
- HTTPS: 469 alive / 115 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 341 alive / 135 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23672
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
