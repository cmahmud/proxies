# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 439
- HTTP: 104 alive / 80 gold
- HTTPS: 90 alive / 25 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47657
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
