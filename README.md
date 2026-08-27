# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 415
- HTTP: 103 alive / 71 gold
- HTTPS: 126 alive / 25 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41890
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
