# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 293
- HTTP: 106 alive / 76 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 76 alive / 66 gold
- SOCKS5: 152 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47883
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
