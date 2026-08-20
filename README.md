# SyndProxy private pool

## Current pool

- Alive now: 1297
- Gold now: 568
- HTTP: 496 alive / 190 gold
- HTTPS: 369 alive / 93 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 219 alive / 137 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22941
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
