# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 351
- HTTP: 116 alive / 74 gold
- HTTPS: 61 alive / 22 gold
- SOCKS4: 129 alive / 110 gold
- SOCKS5: 173 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47982
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
