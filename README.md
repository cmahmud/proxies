# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 398
- HTTP: 89 alive / 55 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41688
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
