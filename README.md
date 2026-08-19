# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 342
- HTTP: 363 alive / 62 gold
- HTTPS: 188 alive / 17 gold
- SOCKS4: 211 alive / 131 gold
- SOCKS5: 208 alive / 132 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20046
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
