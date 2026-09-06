# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 388
- HTTP: 99 alive / 74 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 165 alive / 148 gold
- SOCKS5: 169 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48206
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
