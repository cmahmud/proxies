# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 448
- HTTP: 105 alive / 79 gold
- HTTPS: 113 alive / 30 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47548
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
