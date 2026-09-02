# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 436
- HTTP: 111 alive / 74 gold
- HTTPS: 106 alive / 24 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47570
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
