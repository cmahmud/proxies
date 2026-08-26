# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 397
- HTTP: 145 alive / 69 gold
- HTTPS: 124 alive / 23 gold
- SOCKS4: 168 alive / 149 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39577
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
