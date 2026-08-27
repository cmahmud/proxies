# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 397
- HTTP: 92 alive / 57 gold
- HTTPS: 108 alive / 13 gold
- SOCKS4: 184 alive / 167 gold
- SOCKS5: 192 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41523
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
