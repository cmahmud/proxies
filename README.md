# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 407
- HTTP: 83 alive / 62 gold
- HTTPS: 106 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47213
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
