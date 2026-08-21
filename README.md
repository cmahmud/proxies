# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 396
- HTTP: 305 alive / 78 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 251 alive / 150 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29551
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
