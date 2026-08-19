# SyndProxy private pool

## Current pool

- Alive now: 1254
- Gold now: 384
- HTTP: 404 alive / 89 gold
- HTTPS: 285 alive / 20 gold
- SOCKS4: 255 alive / 138 gold
- SOCKS5: 310 alive / 137 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21491
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
