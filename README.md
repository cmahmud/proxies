# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 413
- HTTP: 294 alive / 96 gold
- HTTPS: 188 alive / 30 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 224 alive / 142 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32534
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
