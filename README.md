# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 378
- HTTP: 90 alive / 63 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 168 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38905
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
