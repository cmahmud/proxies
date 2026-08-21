# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 400
- HTTP: 367 alive / 79 gold
- HTTPS: 215 alive / 21 gold
- SOCKS4: 214 alive / 139 gold
- SOCKS5: 257 alive / 161 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29553
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
