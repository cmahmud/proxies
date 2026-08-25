# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 417
- HTTP: 101 alive / 71 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37118
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
