# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 345
- HTTP: 110 alive / 80 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 121 alive / 98 gold
- SOCKS5: 169 alive / 142 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47964
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
