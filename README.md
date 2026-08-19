# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 411
- HTTP: 375 alive / 81 gold
- HTTPS: 240 alive / 15 gold
- SOCKS4: 265 alive / 156 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 131729
- Ever alive: 20796
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
