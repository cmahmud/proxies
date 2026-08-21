# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 401
- HTTP: 357 alive / 79 gold
- HTTPS: 232 alive / 21 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 260 alive / 153 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29548
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
