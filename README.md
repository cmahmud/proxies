# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 436
- HTTP: 112 alive / 74 gold
- HTTPS: 99 alive / 24 gold
- SOCKS4: 189 alive / 162 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47570
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
