# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 339
- HTTP: 360 alive / 58 gold
- HTTPS: 195 alive / 14 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 208 alive / 135 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20041
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
