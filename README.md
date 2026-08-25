# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 415
- HTTP: 98 alive / 67 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37107
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
