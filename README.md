# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 376
- HTTP: 83 alive / 58 gold
- HTTPS: 66 alive / 9 gold
- SOCKS4: 161 alive / 153 gold
- SOCKS5: 167 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43349
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
