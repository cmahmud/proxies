# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 393
- HTTP: 83 alive / 61 gold
- HTTPS: 91 alive / 17 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43397
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
