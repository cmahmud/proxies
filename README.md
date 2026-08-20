# SyndProxy private pool

## Current pool

- Alive now: 723
- Gold now: 383
- HTTP: 190 alive / 71 gold
- HTTPS: 106 alive / 15 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 218 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25805
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
