# SyndProxy private pool

## Current pool

- Alive now: 1284
- Gold now: 405
- HTTP: 425 alive / 95 gold
- HTTPS: 355 alive / 16 gold
- SOCKS4: 241 alive / 130 gold
- SOCKS5: 263 alive / 164 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21418
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
