# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 293
- HTTP: 102 alive / 75 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 75 alive / 66 gold
- SOCKS5: 155 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47901
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
