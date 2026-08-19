# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 407
- HTTP: 379 alive / 94 gold
- HTTPS: 260 alive / 14 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 324 alive / 150 gold

## Historical pool

- Discovered: 131841
- Ever alive: 21183
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
