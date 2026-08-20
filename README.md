# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 378
- HTTP: 195 alive / 67 gold
- HTTPS: 114 alive / 14 gold
- SOCKS4: 187 alive / 139 gold
- SOCKS5: 220 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25811
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
