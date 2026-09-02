# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 436
- HTTP: 117 alive / 78 gold
- HTTPS: 120 alive / 22 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47581
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
