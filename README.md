# SyndProxy private pool

## Current pool

- Alive now: 1413
- Gold now: 557
- HTTP: 548 alive / 180 gold
- HTTPS: 407 alive / 91 gold
- SOCKS4: 214 alive / 130 gold
- SOCKS5: 244 alive / 156 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22991
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
