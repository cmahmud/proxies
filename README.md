# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 415
- HTTP: 88 alive / 66 gold
- HTTPS: 102 alive / 24 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47246
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
