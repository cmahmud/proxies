# SyndProxy private pool

## Current pool

- Alive now: 1344
- Gold now: 429
- HTTP: 475 alive / 95 gold
- HTTPS: 298 alive / 24 gold
- SOCKS4: 249 alive / 148 gold
- SOCKS5: 322 alive / 162 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22439
- Ever gold: 900

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
