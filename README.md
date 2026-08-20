# SyndProxy private pool

## Current pool

- Alive now: 1560
- Gold now: 605
- HTTP: 553 alive / 198 gold
- HTTPS: 451 alive / 98 gold
- SOCKS4: 246 alive / 147 gold
- SOCKS5: 310 alive / 162 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23607
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
