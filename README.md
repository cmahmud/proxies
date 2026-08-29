# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 376
- HTTP: 82 alive / 60 gold
- HTTPS: 71 alive / 8 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 167 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43347
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
