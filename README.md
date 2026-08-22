# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 409
- HTTP: 192 alive / 85 gold
- HTTPS: 135 alive / 27 gold
- SOCKS4: 199 alive / 139 gold
- SOCKS5: 219 alive / 158 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31423
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
