# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 339
- HTTP: 110 alive / 79 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 115 alive / 95 gold
- SOCKS5: 170 alive / 142 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47961
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
