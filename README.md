# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 438
- HTTP: 102 alive / 78 gold
- HTTPS: 82 alive / 23 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47576
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
