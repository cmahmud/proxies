# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 401
- HTTP: 77 alive / 50 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41676
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
