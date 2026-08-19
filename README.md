# SyndProxy private pool

## Current pool

- Alive now: 1288
- Gold now: 382
- HTTP: 423 alive / 86 gold
- HTTPS: 291 alive / 16 gold
- SOCKS4: 250 alive / 139 gold
- SOCKS5: 324 alive / 141 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21477
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
