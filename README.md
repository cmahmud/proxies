# SyndProxy private pool

## Current pool

- Alive now: 1386
- Gold now: 398
- HTTP: 484 alive / 92 gold
- HTTPS: 313 alive / 15 gold
- SOCKS4: 262 alive / 146 gold
- SOCKS5: 327 alive / 145 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21687
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
