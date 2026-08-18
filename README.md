# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 282
- HTTP: 305 alive / 34 gold
- HTTPS: 221 alive / 5 gold
- SOCKS4: 224 alive / 134 gold
- SOCKS5: 218 alive / 109 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11407
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
