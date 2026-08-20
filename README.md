# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 404
- HTTP: 175 alive / 76 gold
- HTTPS: 134 alive / 23 gold
- SOCKS4: 217 alive / 149 gold
- SOCKS5: 213 alive / 156 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27335
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
