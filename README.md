# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 287
- HTTP: 324 alive / 26 gold
- HTTPS: 157 alive / 4 gold
- SOCKS4: 208 alive / 139 gold
- SOCKS5: 211 alive / 118 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13451
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
