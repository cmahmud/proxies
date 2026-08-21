# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 413
- HTTP: 316 alive / 85 gold
- HTTPS: 253 alive / 23 gold
- SOCKS4: 203 alive / 151 gold
- SOCKS5: 249 alive / 154 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29929
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
