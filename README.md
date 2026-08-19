# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 481
- HTTP: 334 alive / 124 gold
- HTTPS: 213 alive / 70 gold
- SOCKS4: 228 alive / 140 gold
- SOCKS5: 259 alive / 147 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16875
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
