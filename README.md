# SyndProxy private pool

## Current pool

- Alive now: 1490
- Gold now: 607
- HTTP: 562 alive / 219 gold
- HTTPS: 476 alive / 116 gold
- SOCKS4: 218 alive / 133 gold
- SOCKS5: 234 alive / 139 gold

## Historical pool

- Discovered: 140789
- Ever alive: 23780
- Ever gold: 960

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
