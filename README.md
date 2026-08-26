# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 413
- HTTP: 103 alive / 69 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38950
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
