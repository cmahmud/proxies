# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 415
- HTTP: 100 alive / 66 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 173 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37053
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
