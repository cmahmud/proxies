# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 376
- HTTP: 96 alive / 60 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 154 alive / 142 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38848
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
