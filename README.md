# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 415
- HTTP: 100 alive / 70 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38022
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
