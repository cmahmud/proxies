# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 447
- HTTP: 100 alive / 77 gold
- HTTPS: 106 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47541
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
