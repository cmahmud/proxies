# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 439
- HTTP: 114 alive / 81 gold
- HTTPS: 102 alive / 25 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47657
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
