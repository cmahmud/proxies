# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 413
- HTTP: 93 alive / 70 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37122
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
