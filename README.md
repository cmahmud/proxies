# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 381
- HTTP: 203 alive / 68 gold
- HTTPS: 99 alive / 17 gold
- SOCKS4: 193 alive / 139 gold
- SOCKS5: 218 alive / 157 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25812
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
