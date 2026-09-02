# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 437
- HTTP: 102 alive / 78 gold
- HTTPS: 73 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47673
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
