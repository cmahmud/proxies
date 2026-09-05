# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 296
- HTTP: 103 alive / 75 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 73 alive / 67 gold
- SOCKS5: 156 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47902
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
