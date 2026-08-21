# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 405
- HTTP: 361 alive / 80 gold
- HTTPS: 222 alive / 23 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 256 alive / 159 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29554
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
