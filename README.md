# SyndProxy private pool

## Current pool

- Alive now: 1285
- Gold now: 594
- HTTP: 465 alive / 190 gold
- HTTPS: 331 alive / 97 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 249 alive / 160 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23533
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
