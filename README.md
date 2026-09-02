# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 447
- HTTP: 94 alive / 80 gold
- HTTPS: 110 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47539
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
