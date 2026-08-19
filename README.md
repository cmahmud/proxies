# SyndProxy private pool

## Current pool

- Alive now: 1273
- Gold now: 386
- HTTP: 410 alive / 89 gold
- HTTPS: 297 alive / 18 gold
- SOCKS4: 245 alive / 139 gold
- SOCKS5: 321 alive / 140 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21477
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
