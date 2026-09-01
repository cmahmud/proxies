# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 415
- HTTP: 85 alive / 67 gold
- HTTPS: 100 alive / 23 gold
- SOCKS4: 162 alive / 157 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47239
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
