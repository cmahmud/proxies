# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 402
- HTTP: 380 alive / 81 gold
- HTTPS: 279 alive / 24 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 258 alive / 148 gold

## Historical pool

- Discovered: 158234
- Ever alive: 29968
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
