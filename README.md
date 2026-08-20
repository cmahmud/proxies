# SyndProxy private pool

## Current pool

- Alive now: 1795
- Gold now: 649
- HTTP: 755 alive / 242 gold
- HTTPS: 600 alive / 136 gold
- SOCKS4: 205 alive / 132 gold
- SOCKS5: 235 alive / 139 gold

## Historical pool

- Discovered: 142716
- Ever alive: 24514
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
