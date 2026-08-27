# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 397
- HTTP: 88 alive / 53 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41685
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
