# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 394
- HTTP: 93 alive / 62 gold
- HTTPS: 82 alive / 18 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37250
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
