# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 413
- HTTP: 411 alive / 82 gold
- HTTPS: 269 alive / 14 gold
- SOCKS4: 273 alive / 157 gold
- SOCKS5: 255 alive / 160 gold

## Historical pool

- Discovered: 131729
- Ever alive: 20797
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
