# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 347
- HTTP: 110 alive / 80 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 124 alive / 99 gold
- SOCKS5: 175 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47974
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
