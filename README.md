# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 415
- HTTP: 97 alive / 70 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 210 alive / 160 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37125
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
