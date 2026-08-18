# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 335
- HTTP: 277 alive / 47 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 233 alive / 138 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14544
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
