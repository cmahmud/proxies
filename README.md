# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 347
- HTTP: 264 alive / 50 gold
- HTTPS: 187 alive / 14 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 219 alive / 149 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14926
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
