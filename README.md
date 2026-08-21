# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 406
- HTTP: 402 alive / 81 gold
- HTTPS: 292 alive / 26 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 256 alive / 148 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29960
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
