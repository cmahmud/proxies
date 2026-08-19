# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 388
- HTTP: 454 alive / 86 gold
- HTTPS: 322 alive / 12 gold
- SOCKS4: 238 alive / 130 gold
- SOCKS5: 304 alive / 160 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21436
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
