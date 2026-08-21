# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 394
- HTTP: 366 alive / 95 gold
- HTTPS: 294 alive / 30 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 223 alive / 119 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30282
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
