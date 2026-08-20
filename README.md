# SyndProxy private pool

## Current pool

- Alive now: 1537
- Gold now: 583
- HTTP: 557 alive / 196 gold
- HTTPS: 431 alive / 99 gold
- SOCKS4: 249 alive / 138 gold
- SOCKS5: 300 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23327
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
