# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 441
- HTTP: 327 alive / 95 gold
- HTTPS: 219 alive / 34 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 249 alive / 172 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31261
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
