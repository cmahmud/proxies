# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 449
- HTTP: 102 alive / 79 gold
- HTTPS: 107 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47542
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
