# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 301
- HTTP: 369 alive / 65 gold
- HTTPS: 215 alive / 18 gold
- SOCKS4: 201 alive / 117 gold
- SOCKS5: 184 alive / 101 gold

## Historical pool

- Discovered: 109990
- Ever alive: 15648
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
