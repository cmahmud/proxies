# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 393
- HTTP: 333 alive / 102 gold
- HTTPS: 246 alive / 33 gold
- SOCKS4: 216 alive / 120 gold
- SOCKS5: 276 alive / 138 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28037
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
