# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 389
- HTTP: 98 alive / 61 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 168 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37364
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
