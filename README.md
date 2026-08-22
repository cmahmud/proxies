# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 363
- HTTP: 348 alive / 91 gold
- HTTPS: 182 alive / 29 gold
- SOCKS4: 179 alive / 105 gold
- SOCKS5: 237 alive / 138 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32567
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
