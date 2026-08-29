# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 388
- HTTP: 90 alive / 64 gold
- HTTPS: 84 alive / 12 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 166 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43440
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
