# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 381
- HTTP: 300 alive / 89 gold
- HTTPS: 208 alive / 30 gold
- SOCKS4: 180 alive / 123 gold
- SOCKS5: 239 alive / 139 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28874
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
