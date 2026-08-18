# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 286
- HTTP: 246 alive / 37 gold
- HTTPS: 170 alive / 9 gold
- SOCKS4: 208 alive / 140 gold
- SOCKS5: 180 alive / 100 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13984
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
