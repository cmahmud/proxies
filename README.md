# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 408
- HTTP: 448 alive / 91 gold
- HTTPS: 257 alive / 17 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20910
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
