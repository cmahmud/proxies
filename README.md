# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 391
- HTTP: 410 alive / 110 gold
- HTTPS: 279 alive / 29 gold
- SOCKS4: 214 alive / 117 gold
- SOCKS5: 290 alive / 135 gold

## Historical pool

- Discovered: 152257
- Ever alive: 28006
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
