# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 249
- HTTP: 246 alive / 35 gold
- HTTPS: 147 alive / 8 gold
- SOCKS4: 213 alive / 124 gold
- SOCKS5: 207 alive / 82 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9348
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
