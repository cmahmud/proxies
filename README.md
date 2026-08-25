# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 415
- HTTP: 94 alive / 66 gold
- HTTPS: 64 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 174 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37099
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
