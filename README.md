# SyndProxy validated proxy pool

## Current pool

- Alive now: 381
- Gold now: 300
- HTTP: 104 alive / 75 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 78 alive / 66 gold
- SOCKS5: 156 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47876
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
