# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 378
- HTTP: 366 alive / 102 gold
- HTTPS: 250 alive / 31 gold
- SOCKS4: 207 alive / 110 gold
- SOCKS5: 261 alive / 135 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28319
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
