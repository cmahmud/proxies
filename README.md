# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 348
- HTTP: 114 alive / 80 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 126 alive / 101 gold
- SOCKS5: 175 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47976
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
