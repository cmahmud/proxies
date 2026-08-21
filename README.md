# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 395
- HTTP: 323 alive / 81 gold
- HTTPS: 214 alive / 23 gold
- SOCKS4: 200 alive / 134 gold
- SOCKS5: 254 alive / 157 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29551
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
