# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 395
- HTTP: 326 alive / 80 gold
- HTTPS: 203 alive / 23 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 250 alive / 146 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29550
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
