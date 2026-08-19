# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 363
- HTTP: 314 alive / 74 gold
- HTTPS: 219 alive / 17 gold
- SOCKS4: 247 alive / 151 gold
- SOCKS5: 217 alive / 121 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15906
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
