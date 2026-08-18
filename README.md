# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 344
- HTTP: 312 alive / 49 gold
- HTTPS: 201 alive / 13 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 231 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14666
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
