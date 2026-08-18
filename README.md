# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 273
- HTTP: 363 alive / 30 gold
- HTTPS: 117 alive / 5 gold
- SOCKS4: 213 alive / 131 gold
- SOCKS5: 209 alive / 107 gold

## Historical pool

- Discovered: 99053
- Ever alive: 11243
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
