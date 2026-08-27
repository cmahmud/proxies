# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 415
- HTTP: 108 alive / 65 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41306
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
