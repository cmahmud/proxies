# SyndProxy private pool

## Current pool

- Alive now: 1246
- Gold now: 392
- HTTP: 454 alive / 85 gold
- HTTPS: 249 alive / 16 gold
- SOCKS4: 251 alive / 146 gold
- SOCKS5: 292 alive / 145 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21780
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
