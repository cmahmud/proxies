# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 415
- HTTP: 111 alive / 75 gold
- HTTPS: 65 alive / 29 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 168 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
