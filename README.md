# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 354
- HTTP: 124 alive / 78 gold
- HTTPS: 63 alive / 23 gold
- SOCKS4: 129 alive / 108 gold
- SOCKS5: 173 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47980
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
