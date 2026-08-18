# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 280
- HTTP: 366 alive / 31 gold
- HTTPS: 199 alive / 5 gold
- SOCKS4: 224 alive / 134 gold
- SOCKS5: 216 alive / 110 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11378
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
