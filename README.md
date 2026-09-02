# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 448
- HTTP: 105 alive / 81 gold
- HTTPS: 117 alive / 29 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 198 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47557
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
