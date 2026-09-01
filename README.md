# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 461
- HTTP: 138 alive / 89 gold
- HTTPS: 127 alive / 36 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46864
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
