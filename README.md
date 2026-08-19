# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 508
- HTTP: 367 alive / 159 gold
- HTTPS: 249 alive / 90 gold
- SOCKS4: 216 alive / 141 gold
- SOCKS5: 207 alive / 118 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18373
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
