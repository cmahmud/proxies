# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 415
- HTTP: 108 alive / 69 gold
- HTTPS: 79 alive / 19 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38023
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
