# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 388
- HTTP: 286 alive / 86 gold
- HTTPS: 222 alive / 27 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 235 alive / 132 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30905
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
