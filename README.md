# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 371
- HTTP: 95 alive / 63 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 150 alive / 143 gold
- SOCKS5: 168 alive / 148 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38868
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
