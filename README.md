# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 394
- HTTP: 87 alive / 51 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41663
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
