# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 326
- HTTP: 95 alive / 67 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 124 alive / 109 gold
- SOCKS5: 141 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49546
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
