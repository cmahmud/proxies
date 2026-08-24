# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 390
- HTTP: 101 alive / 61 gold
- HTTPS: 54 alive / 13 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33193
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
