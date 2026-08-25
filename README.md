# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 397
- HTTP: 94 alive / 63 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37252
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
