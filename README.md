# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 392
- HTTP: 389 alive / 91 gold
- HTTPS: 277 alive / 13 gold
- SOCKS4: 240 alive / 139 gold
- SOCKS5: 284 alive / 149 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21059
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
