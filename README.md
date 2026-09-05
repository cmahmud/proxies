# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 292
- HTTP: 102 alive / 72 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 70 alive / 67 gold
- SOCKS5: 154 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47909
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
