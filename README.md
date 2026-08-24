# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 389
- HTTP: 102 alive / 61 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 160 alive / 156 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33194
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
