# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 476
- HTTP: 335 alive / 123 gold
- HTTPS: 235 alive / 72 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 241 alive / 141 gold

## Historical pool

- Discovered: 114270
- Ever alive: 16909
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
