# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 377
- HTTP: 296 alive / 82 gold
- HTTPS: 217 alive / 23 gold
- SOCKS4: 217 alive / 134 gold
- SOCKS5: 216 alive / 138 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29367
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
