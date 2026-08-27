# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 415
- HTTP: 116 alive / 69 gold
- HTTPS: 129 alive / 18 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41335
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
