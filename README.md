# SyndProxy private pool

## Current pool

- Alive now: 1280
- Gold now: 388
- HTTP: 454 alive / 95 gold
- HTTPS: 307 alive / 21 gold
- SOCKS4: 219 alive / 130 gold
- SOCKS5: 300 alive / 142 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22119
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
