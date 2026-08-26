# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 369
- HTTP: 86 alive / 56 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 155 alive / 142 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38883
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
