# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 395
- HTTP: 326 alive / 82 gold
- HTTPS: 213 alive / 23 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 248 alive / 144 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29549
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
