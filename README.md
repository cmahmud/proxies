# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 415
- HTTP: 87 alive / 66 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48853
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
