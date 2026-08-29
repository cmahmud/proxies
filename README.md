# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 398
- HTTP: 82 alive / 63 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43387
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
