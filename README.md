# SyndProxy private pool

## Current pool

- Alive now: 1264
- Gold now: 386
- HTTP: 408 alive / 90 gold
- HTTPS: 284 alive / 18 gold
- SOCKS4: 253 alive / 139 gold
- SOCKS5: 319 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21479
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
