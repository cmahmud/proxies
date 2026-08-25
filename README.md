# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 419
- HTTP: 107 alive / 71 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37117
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
