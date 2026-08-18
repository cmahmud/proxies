# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 318
- HTTP: 295 alive / 38 gold
- HTTPS: 203 alive / 10 gold
- SOCKS4: 246 alive / 138 gold
- SOCKS5: 241 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14241
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
