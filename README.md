# SyndProxy private pool

## Current pool

- Alive now: 1566
- Gold now: 668
- HTTP: 571 alive / 253 gold
- HTTPS: 442 alive / 129 gold
- SOCKS4: 207 alive / 127 gold
- SOCKS5: 346 alive / 159 gold

## Historical pool

- Discovered: 143490
- Ever alive: 24811
- Ever gold: 1049

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
