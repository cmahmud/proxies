# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 376
- HTTP: 83 alive / 62 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 169 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43436
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
