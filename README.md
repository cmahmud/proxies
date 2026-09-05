# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 293
- HTTP: 105 alive / 75 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 76 alive / 65 gold
- SOCKS5: 158 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47898
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
