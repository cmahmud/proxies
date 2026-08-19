# SyndProxy private pool

## Current pool

- Alive now: 1289
- Gold now: 405
- HTTP: 446 alive / 95 gold
- HTTPS: 351 alive / 15 gold
- SOCKS4: 239 alive / 130 gold
- SOCKS5: 253 alive / 165 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21409
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
