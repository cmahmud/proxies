# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 529
- HTTP: 459 alive / 184 gold
- HTTPS: 261 alive / 101 gold
- SOCKS4: 216 alive / 114 gold
- SOCKS5: 199 alive / 130 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19404
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
