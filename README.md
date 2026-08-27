# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 415
- HTTP: 107 alive / 69 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40980
- Ever gold: 1314

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
