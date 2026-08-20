# SyndProxy private pool

## Current pool

- Alive now: 1612
- Gold now: 674
- HTTP: 606 alive / 258 gold
- HTTPS: 449 alive / 129 gold
- SOCKS4: 212 alive / 128 gold
- SOCKS5: 345 alive / 159 gold

## Historical pool

- Discovered: 143490
- Ever alive: 24811
- Ever gold: 1049

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
