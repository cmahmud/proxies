# SyndProxy private pool

## Current pool

- Alive now: 1369
- Gold now: 432
- HTTP: 499 alive / 92 gold
- HTTPS: 309 alive / 23 gold
- SOCKS4: 242 alive / 151 gold
- SOCKS5: 319 alive / 166 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22433
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
