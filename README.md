# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 388
- HTTP: 345 alive / 107 gold
- HTTPS: 248 alive / 30 gold
- SOCKS4: 217 alive / 116 gold
- SOCKS5: 303 alive / 135 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28024
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
