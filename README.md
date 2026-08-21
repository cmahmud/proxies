# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 405
- HTTP: 324 alive / 82 gold
- HTTPS: 222 alive / 22 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 256 alive / 153 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29549
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
