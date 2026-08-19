# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 397
- HTTP: 385 alive / 88 gold
- HTTPS: 261 alive / 22 gold
- SOCKS4: 222 alive / 138 gold
- SOCKS5: 293 alive / 149 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22157
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
