# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 373
- HTTP: 103 alive / 64 gold
- HTTPS: 68 alive / 14 gold
- SOCKS4: 153 alive / 143 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38811
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
