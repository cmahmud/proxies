# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 415
- HTTP: 87 alive / 58 gold
- HTTPS: 42 alive / 24 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47094
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
