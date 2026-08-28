# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 397
- HTTP: 81 alive / 56 gold
- HTTPS: 39 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42843
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
