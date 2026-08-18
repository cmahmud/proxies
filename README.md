# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 343
- HTTP: 293 alive / 56 gold
- HTTPS: 177 alive / 13 gold
- SOCKS4: 232 alive / 139 gold
- SOCKS5: 223 alive / 135 gold

## Historical pool

- Discovered: 107138
- Ever alive: 15023
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
