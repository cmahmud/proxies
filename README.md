# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 276
- HTTP: 299 alive / 34 gold
- HTTPS: 161 alive / 4 gold
- SOCKS4: 229 alive / 133 gold
- SOCKS5: 213 alive / 105 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11413
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
