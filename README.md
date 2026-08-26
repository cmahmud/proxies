# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 423
- HTTP: 113 alive / 74 gold
- HTTPS: 87 alive / 20 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37925
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
