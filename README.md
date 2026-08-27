# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 415
- HTTP: 102 alive / 72 gold
- HTTPS: 107 alive / 21 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41957
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
