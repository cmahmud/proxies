# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 394
- HTTP: 88 alive / 66 gold
- HTTPS: 82 alive / 14 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 166 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43378
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
