# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 396
- HTTP: 320 alive / 97 gold
- HTTPS: 250 alive / 27 gold
- SOCKS4: 234 alive / 133 gold
- SOCKS5: 242 alive / 139 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25110
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
