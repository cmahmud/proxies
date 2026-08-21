# SyndProxy private pool

## Current pool

- Alive now: 1239
- Gold now: 448
- HTTP: 449 alive / 106 gold
- HTTPS: 301 alive / 27 gold
- SOCKS4: 208 alive / 153 gold
- SOCKS5: 281 alive / 162 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28575
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
