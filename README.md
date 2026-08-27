# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 403
- HTTP: 96 alive / 62 gold
- HTTPS: 108 alive / 16 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41415
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
