# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 332
- HTTP: 83 alive / 61 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 156 alive / 135 gold
- SOCKS5: 150 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48352
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
