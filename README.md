# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 397
- HTTP: 125 alive / 71 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33279
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
