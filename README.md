# SyndProxy private pool

## Current pool

- Alive now: 1431
- Gold now: 437
- HTTP: 547 alive / 95 gold
- HTTPS: 322 alive / 24 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 322 alive / 168 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22430
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
