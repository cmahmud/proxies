# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 388
- HTTP: 114 alive / 58 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33511
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
