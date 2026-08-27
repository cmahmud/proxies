# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 415
- HTTP: 94 alive / 64 gold
- HTTPS: 114 alive / 21 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41445
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
