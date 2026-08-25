# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 400
- HTTP: 103 alive / 64 gold
- HTTPS: 78 alive / 19 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 166 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37293
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
