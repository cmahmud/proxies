# SyndProxy private pool

## Current pool

- Alive now: 1305
- Gold now: 432
- HTTP: 473 alive / 93 gold
- HTTPS: 308 alive / 23 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 300 alive / 166 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22397
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
