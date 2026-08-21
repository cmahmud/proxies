# SyndProxy private pool

## Current pool

- Alive now: 1313
- Gold now: 439
- HTTP: 477 alive / 106 gold
- HTTPS: 347 alive / 33 gold
- SOCKS4: 225 alive / 138 gold
- SOCKS5: 264 alive / 162 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30361
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
