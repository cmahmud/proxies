# SyndProxy private pool

## Current pool

- Alive now: 1435
- Gold now: 420
- HTTP: 538 alive / 87 gold
- HTTPS: 363 alive / 18 gold
- SOCKS4: 257 alive / 156 gold
- SOCKS5: 277 alive / 159 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20848
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
