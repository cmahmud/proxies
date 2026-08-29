# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 390
- HTTP: 81 alive / 64 gold
- HTTPS: 61 alive / 11 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43384
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
