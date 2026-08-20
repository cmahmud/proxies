# SyndProxy private pool

## Current pool

- Alive now: 1563
- Gold now: 556
- HTTP: 631 alive / 180 gold
- HTTPS: 448 alive / 89 gold
- SOCKS4: 233 alive / 128 gold
- SOCKS5: 251 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 23011
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
