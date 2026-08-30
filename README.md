# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 437
- HTTP: 102 alive / 81 gold
- HTTPS: 44 alive / 26 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43685
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
