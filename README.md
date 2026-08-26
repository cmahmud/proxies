# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 383
- HTTP: 110 alive / 63 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 157 alive / 145 gold
- SOCKS5: 175 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38916
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
