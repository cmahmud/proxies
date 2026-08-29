# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 393
- HTTP: 85 alive / 61 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43397
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
