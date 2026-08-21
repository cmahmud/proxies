# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 399
- HTTP: 334 alive / 79 gold
- HTTPS: 210 alive / 22 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 258 alive / 159 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29552
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
