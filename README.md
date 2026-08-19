# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 363
- HTTP: 375 alive / 71 gold
- HTTPS: 249 alive / 13 gold
- SOCKS4: 217 alive / 129 gold
- SOCKS5: 252 alive / 150 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20368
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
