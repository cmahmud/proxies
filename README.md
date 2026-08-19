# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 506
- HTTP: 388 alive / 148 gold
- HTTPS: 284 alive / 88 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 215 alive / 153 gold

## Historical pool

- Discovered: 118125
- Ever alive: 17781
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
