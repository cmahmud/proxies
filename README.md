# SyndProxy private pool

## Current pool

- Alive now: 1278
- Gold now: 397
- HTTP: 430 alive / 89 gold
- HTTPS: 317 alive / 21 gold
- SOCKS4: 236 alive / 136 gold
- SOCKS5: 295 alive / 151 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22176
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
