# SyndProxy private pool

## Current pool

- Alive now: 1333
- Gold now: 212
- HTTP: 549 alive / 29 gold
- HTTPS: 270 alive / 10 gold
- SOCKS4: 292 alive / 99 gold
- SOCKS5: 222 alive / 74 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
