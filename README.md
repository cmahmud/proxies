# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 379
- HTTP: 165 alive / 73 gold
- HTTPS: 156 alive / 14 gold
- SOCKS4: 211 alive / 153 gold
- SOCKS5: 195 alive / 139 gold

## Historical pool

- Discovered: 147653
- Ever alive: 25891
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
