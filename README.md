# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 340
- HTTP: 355 alive / 58 gold
- HTTPS: 198 alive / 16 gold
- SOCKS4: 208 alive / 132 gold
- SOCKS5: 204 alive / 134 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20044
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
