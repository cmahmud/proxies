# SyndProxy private pool

## Current pool

- Alive now: 1436
- Gold now: 413
- HTTP: 599 alive / 90 gold
- HTTPS: 365 alive / 36 gold
- SOCKS4: 229 alive / 141 gold
- SOCKS5: 243 alive / 146 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31721
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
