# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 342
- HTTP: 379 alive / 63 gold
- HTTPS: 215 alive / 11 gold
- SOCKS4: 238 alive / 141 gold
- SOCKS5: 219 alive / 127 gold

## Historical pool

- Discovered: 129268
- Ever alive: 20246
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
