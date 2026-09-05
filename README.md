# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 294
- HTTP: 104 alive / 74 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 71 alive / 67 gold
- SOCKS5: 155 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47904
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
