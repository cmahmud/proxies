# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 407
- HTTP: 345 alive / 80 gold
- HTTPS: 229 alive / 27 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29555
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
