# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 442
- HTTP: 401 alive / 106 gold
- HTTPS: 281 alive / 28 gold
- SOCKS4: 204 alive / 152 gold
- SOCKS5: 267 alive / 156 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28575
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
