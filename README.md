# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 364
- HTTP: 186 alive / 68 gold
- HTTPS: 139 alive / 20 gold
- SOCKS4: 186 alive / 135 gold
- SOCKS5: 194 alive / 141 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26689
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
