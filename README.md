# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 413
- HTTP: 367 alive / 84 gold
- HTTPS: 283 alive / 22 gold
- SOCKS4: 205 alive / 151 gold
- SOCKS5: 256 alive / 156 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29949
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
