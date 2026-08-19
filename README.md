# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 408
- HTTP: 351 alive / 85 gold
- HTTPS: 208 alive / 30 gold
- SOCKS4: 229 alive / 158 gold
- SOCKS5: 208 alive / 135 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18228
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
