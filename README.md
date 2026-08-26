# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 376
- HTTP: 105 alive / 65 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 156 alive / 144 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38791
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
