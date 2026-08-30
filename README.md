# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 415
- HTTP: 116 alive / 81 gold
- HTTPS: 58 alive / 27 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 170 alive / 157 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43698
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
