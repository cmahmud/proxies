# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 457
- HTTP: 139 alive / 88 gold
- HTTPS: 102 alive / 33 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 215 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45349
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
