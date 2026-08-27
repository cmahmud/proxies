# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 415
- HTTP: 101 alive / 69 gold
- HTTPS: 117 alive / 18 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41407
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
