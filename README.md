# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 379
- HTTP: 261 alive / 65 gold
- HTTPS: 170 alive / 23 gold
- SOCKS4: 202 alive / 140 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 157407
- Ever alive: 29680
- Ever gold: 1136

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
