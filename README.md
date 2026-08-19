# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 306
- HTTP: 367 alive / 64 gold
- HTTPS: 233 alive / 19 gold
- SOCKS4: 215 alive / 117 gold
- SOCKS5: 200 alive / 106 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15593
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
