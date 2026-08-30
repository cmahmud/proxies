# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 415
- HTTP: 132 alive / 78 gold
- HTTPS: 82 alive / 27 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 280 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43845
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
