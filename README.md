# SyndProxy private pool

## Current pool

- Alive now: 1460
- Gold now: 392
- HTTP: 544 alive / 101 gold
- HTTPS: 366 alive / 21 gold
- SOCKS4: 232 alive / 129 gold
- SOCKS5: 318 alive / 141 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22501
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
