# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 382
- HTTP: 108 alive / 59 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 156 alive / 149 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38930
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
