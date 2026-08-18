# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 359
- HTTP: 328 alive / 54 gold
- HTTPS: 208 alive / 13 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 240 alive / 151 gold

## Historical pool

- Discovered: 107128
- Ever alive: 14876
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
