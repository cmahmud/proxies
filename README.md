# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 419
- HTTP: 441 alive / 100 gold
- HTTPS: 283 alive / 24 gold
- SOCKS4: 227 alive / 139 gold
- SOCKS5: 246 alive / 156 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30425
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
