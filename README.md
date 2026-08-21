# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 425
- HTTP: 296 alive / 108 gold
- HTTPS: 214 alive / 30 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 256 alive / 139 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30803
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
