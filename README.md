# SyndProxy private pool

## Current pool

- Alive now: 1419
- Gold now: 436
- HTTP: 542 alive / 95 gold
- HTTPS: 323 alive / 23 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 319 alive / 168 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22428
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
