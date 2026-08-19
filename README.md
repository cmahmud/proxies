# SyndProxy private pool

## Current pool

- Alive now: 1263
- Gold now: 354
- HTTP: 424 alive / 87 gold
- HTTPS: 284 alive / 20 gold
- SOCKS4: 236 alive / 112 gold
- SOCKS5: 319 alive / 135 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22052
- Ever gold: 892

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
