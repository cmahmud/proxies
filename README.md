# SyndProxy private pool

## Current pool

- Alive now: 1542
- Gold now: 550
- HTTP: 623 alive / 177 gold
- HTTPS: 442 alive / 89 gold
- SOCKS4: 234 alive / 127 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 138813
- Ever alive: 23030
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
