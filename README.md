# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 380
- HTTP: 232 alive / 67 gold
- HTTPS: 177 alive / 23 gold
- SOCKS4: 196 alive / 140 gold
- SOCKS5: 207 alive / 150 gold

## Historical pool

- Discovered: 157407
- Ever alive: 29680
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
