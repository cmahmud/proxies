# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 433
- HTTP: 94 alive / 75 gold
- HTTPS: 66 alive / 29 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47019
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
