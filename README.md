# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 381
- HTTP: 317 alive / 88 gold
- HTTPS: 179 alive / 23 gold
- SOCKS4: 202 alive / 114 gold
- SOCKS5: 257 alive / 156 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32397
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
