# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 415
- HTTP: 105 alive / 78 gold
- HTTPS: 83 alive / 27 gold
- SOCKS4: 173 alive / 151 gold
- SOCKS5: 267 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43802
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
