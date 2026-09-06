# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 348
- HTTP: 114 alive / 81 gold
- HTTPS: 59 alive / 23 gold
- SOCKS4: 123 alive / 99 gold
- SOCKS5: 174 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47974
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
