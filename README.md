# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 341
- HTTP: 344 alive / 65 gold
- HTTPS: 206 alive / 15 gold
- SOCKS4: 249 alive / 137 gold
- SOCKS5: 208 alive / 124 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15343
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
