# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 415
- HTTP: 103 alive / 71 gold
- HTTPS: 110 alive / 15 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42571
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
