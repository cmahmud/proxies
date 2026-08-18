# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 281
- HTTP: 294 alive / 29 gold
- HTTPS: 224 alive / 6 gold
- SOCKS4: 210 alive / 126 gold
- SOCKS5: 221 alive / 120 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13092
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
