# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 397
- HTTP: 74 alive / 51 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41681
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
