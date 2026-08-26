# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 408
- HTTP: 108 alive / 67 gold
- HTTPS: 81 alive / 12 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38123
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
