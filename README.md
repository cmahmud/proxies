# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 415
- HTTP: 102 alive / 61 gold
- HTTPS: 107 alive / 23 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41483
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
