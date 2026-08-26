# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 374
- HTTP: 105 alive / 64 gold
- HTTPS: 70 alive / 14 gold
- SOCKS4: 153 alive / 144 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38813
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
