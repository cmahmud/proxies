# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 415
- HTTP: 152 alive / 78 gold
- HTTPS: 162 alive / 23 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40333
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
