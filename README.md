# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 408
- HTTP: 96 alive / 72 gold
- HTTPS: 32 alive / 15 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48248
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
