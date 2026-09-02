# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 436
- HTTP: 99 alive / 78 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 181 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47679
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
