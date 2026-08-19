# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 391
- HTTP: 327 alive / 68 gold
- HTTPS: 233 alive / 15 gold
- SOCKS4: 244 alive / 148 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20442
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
