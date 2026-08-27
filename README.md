# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 415
- HTTP: 101 alive / 66 gold
- HTTPS: 188 alive / 18 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40696
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
