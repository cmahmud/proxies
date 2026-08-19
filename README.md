# SyndProxy private pool

## Current pool

- Alive now: 1169
- Gold now: 502
- HTTP: 442 alive / 192 gold
- HTTPS: 311 alive / 115 gold
- SOCKS4: 211 alive / 81 gold
- SOCKS5: 205 alive / 114 gold

## Historical pool

- Discovered: 124849
- Ever alive: 19397
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
