# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 436
- HTTP: 98 alive / 77 gold
- HTTPS: 92 alive / 25 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47679
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
