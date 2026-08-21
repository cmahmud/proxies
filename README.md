# SyndProxy private pool

## Current pool

- Alive now: 1305
- Gold now: 431
- HTTP: 514 alive / 102 gold
- HTTPS: 323 alive / 29 gold
- SOCKS4: 222 alive / 139 gold
- SOCKS5: 246 alive / 161 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30413
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
