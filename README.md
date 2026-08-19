# SyndProxy private pool

## Current pool

- Alive now: 1246
- Gold now: 392
- HTTP: 454 alive / 84 gold
- HTTPS: 256 alive / 16 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 293 alive / 145 gold

## Historical pool

- Discovered: 134447
- Ever alive: 21780
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
