# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 436
- HTTP: 107 alive / 76 gold
- HTTPS: 78 alive / 26 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 182 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47680
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
