# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 522
- HTTP: 351 alive / 160 gold
- HTTPS: 275 alive / 91 gold
- SOCKS4: 201 alive / 141 gold
- SOCKS5: 200 alive / 130 gold

## Historical pool

- Discovered: 119848
- Ever alive: 18423
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
