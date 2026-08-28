# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 397
- HTTP: 81 alive / 57 gold
- HTTPS: 35 alive / 14 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42853
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
