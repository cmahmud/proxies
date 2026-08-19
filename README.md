# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 532
- HTTP: 392 alive / 156 gold
- HTTPS: 243 alive / 88 gold
- SOCKS4: 208 alive / 148 gold
- SOCKS5: 222 alive / 140 gold

## Historical pool

- Discovered: 119811
- Ever alive: 18036
- Ever gold: 711

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
