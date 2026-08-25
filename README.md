# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 405
- HTTP: 100 alive / 69 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37314
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
