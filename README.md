# SyndProxy validated proxy pool

## Current pool

- Alive now: 687
- Gold now: 469
- HTTP: 147 alive / 95 gold
- HTTPS: 124 alive / 35 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 236 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46206
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
