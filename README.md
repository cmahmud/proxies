# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 398
- HTTP: 104 alive / 67 gold
- HTTPS: 49 alive / 23 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 169 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43650
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
