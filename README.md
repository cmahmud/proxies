# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 361
- HTTP: 125 alive / 79 gold
- HTTPS: 61 alive / 22 gold
- SOCKS4: 141 alive / 114 gold
- SOCKS5: 176 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47987
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
