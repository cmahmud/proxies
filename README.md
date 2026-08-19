# SyndProxy private pool

## Current pool

- Alive now: 1432
- Gold now: 384
- HTTP: 523 alive / 83 gold
- HTTPS: 360 alive / 14 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 309 alive / 141 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21794
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
