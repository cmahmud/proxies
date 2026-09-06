# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 318
- HTTP: 89 alive / 54 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 151 alive / 133 gold
- SOCKS5: 148 alive / 118 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48351
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
