# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 392
- HTTP: 81 alive / 50 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41665
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
