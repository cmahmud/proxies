# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 397
- HTTP: 422 alive / 86 gold
- HTTPS: 235 alive / 25 gold
- SOCKS4: 180 alive / 114 gold
- SOCKS5: 253 alive / 172 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32449
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
