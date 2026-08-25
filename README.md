# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 411
- HTTP: 106 alive / 70 gold
- HTTPS: 79 alive / 22 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37154
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
