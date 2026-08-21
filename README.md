# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 381
- HTTP: 273 alive / 88 gold
- HTTPS: 208 alive / 31 gold
- SOCKS4: 176 alive / 123 gold
- SOCKS5: 235 alive / 139 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28868
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
