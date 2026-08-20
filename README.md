# SyndProxy private pool

## Current pool

- Alive now: 1849
- Gold now: 668
- HTTP: 726 alive / 227 gold
- HTTPS: 568 alive / 124 gold
- SOCKS4: 245 alive / 150 gold
- SOCKS5: 310 alive / 167 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24360
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
