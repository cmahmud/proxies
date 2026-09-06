# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 345
- HTTP: 114 alive / 80 gold
- HTTPS: 63 alive / 23 gold
- SOCKS4: 127 alive / 99 gold
- SOCKS5: 174 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47973
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
