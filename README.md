# SyndProxy private pool

## Current pool

- Alive now: 1313
- Gold now: 386
- HTTP: 461 alive / 90 gold
- HTTPS: 301 alive / 18 gold
- SOCKS4: 273 alive / 137 gold
- SOCKS5: 278 alive / 141 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21557
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
