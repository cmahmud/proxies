# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 400
- HTTP: 98 alive / 67 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 168 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37277
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
