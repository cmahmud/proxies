# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 108 alive / 68 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37162
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
