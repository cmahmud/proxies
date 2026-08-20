# SyndProxy private pool

## Current pool

- Alive now: 1530
- Gold now: 607
- HTTP: 589 alive / 215 gold
- HTTPS: 485 alive / 120 gold
- SOCKS4: 220 alive / 133 gold
- SOCKS5: 236 alive / 139 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23774
- Ever gold: 960

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
