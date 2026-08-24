# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 391
- HTTP: 112 alive / 61 gold
- HTTPS: 65 alive / 14 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33511
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
