# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 391
- HTTP: 85 alive / 62 gold
- HTTPS: 50 alive / 21 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 167 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43648
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
