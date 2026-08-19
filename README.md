# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 347
- HTTP: 366 alive / 68 gold
- HTTPS: 271 alive / 17 gold
- SOCKS4: 194 alive / 108 gold
- SOCKS5: 234 alive / 154 gold

## Historical pool

- Discovered: 112040
- Ever alive: 16338
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
