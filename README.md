# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 413
- HTTP: 108 alive / 72 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 168 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37188
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
