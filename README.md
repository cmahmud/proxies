# SyndProxy private pool

## Current pool

- Alive now: 1172
- Gold now: 408
- HTTP: 377 alive / 94 gold
- HTTPS: 251 alive / 14 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 322 alive / 151 gold

## Historical pool

- Discovered: 131841
- Ever alive: 21195
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
