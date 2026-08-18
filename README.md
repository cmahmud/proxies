# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 333
- HTTP: 327 alive / 45 gold
- HTTPS: 178 alive / 11 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 224 alive / 139 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14416
- Ever gold: 459

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
