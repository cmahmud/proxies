# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 387
- HTTP: 86 alive / 63 gold
- HTTPS: 61 alive / 12 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43382
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
