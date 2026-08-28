# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 391
- HTTP: 86 alive / 65 gold
- HTTPS: 70 alive / 12 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43222
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
