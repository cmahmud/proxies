# SyndProxy private pool

## Current pool

- Alive now: 1285
- Gold now: 404
- HTTP: 437 alive / 94 gold
- HTTPS: 352 alive / 16 gold
- SOCKS4: 243 alive / 131 gold
- SOCKS5: 253 alive / 163 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21407
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
