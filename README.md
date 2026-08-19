# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 511
- HTTP: 391 alive / 170 gold
- HTTPS: 310 alive / 86 gold
- SOCKS4: 224 alive / 129 gold
- SOCKS5: 216 alive / 126 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19764
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
