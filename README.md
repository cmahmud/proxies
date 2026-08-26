# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 374
- HTTP: 105 alive / 65 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 150 alive / 142 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38830
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
