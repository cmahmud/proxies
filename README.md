# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 400
- HTTP: 358 alive / 78 gold
- HTTPS: 221 alive / 22 gold
- SOCKS4: 239 alive / 147 gold
- SOCKS5: 265 alive / 153 gold

## Historical pool

- Discovered: 156436
- Ever alive: 29548
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
