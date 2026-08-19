# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 420
- HTTP: 390 alive / 91 gold
- HTTPS: 279 alive / 23 gold
- SOCKS4: 235 alive / 140 gold
- SOCKS5: 295 alive / 166 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22255
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
