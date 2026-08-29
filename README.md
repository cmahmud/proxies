# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 383
- HTTP: 83 alive / 67 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 158 alive / 149 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43251
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
