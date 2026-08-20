# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 381
- HTTP: 205 alive / 69 gold
- HTTPS: 108 alive / 14 gold
- SOCKS4: 190 alive / 139 gold
- SOCKS5: 222 alive / 159 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25807
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
