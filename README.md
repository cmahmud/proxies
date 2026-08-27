# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 423
- HTTP: 107 alive / 78 gold
- HTTPS: 112 alive / 20 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42119
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
