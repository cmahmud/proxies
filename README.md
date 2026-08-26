# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 377
- HTTP: 105 alive / 67 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 149 alive / 142 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38828
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
