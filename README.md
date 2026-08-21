# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 402
- HTTP: 265 alive / 74 gold
- HTTPS: 151 alive / 24 gold
- SOCKS4: 239 alive / 156 gold
- SOCKS5: 248 alive / 148 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29611
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
