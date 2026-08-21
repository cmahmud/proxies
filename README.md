# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 387
- HTTP: 310 alive / 78 gold
- HTTPS: 205 alive / 23 gold
- SOCKS4: 206 alive / 135 gold
- SOCKS5: 251 alive / 151 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29551
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
