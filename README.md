# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 523
- HTTP: 381 alive / 160 gold
- HTTPS: 258 alive / 90 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 219 alive / 134 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18523
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
