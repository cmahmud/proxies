# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 306
- HTTP: 83 alive / 55 gold
- HTTPS: 34 alive / 4 gold
- SOCKS4: 148 alive / 132 gold
- SOCKS5: 150 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48371
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
