# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 438
- HTTP: 126 alive / 75 gold
- HTTPS: 127 alive / 26 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47614
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
