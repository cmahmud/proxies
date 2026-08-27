# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 415
- HTTP: 89 alive / 72 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 174 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41759
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
