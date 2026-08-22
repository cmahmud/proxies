# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 391
- HTTP: 352 alive / 84 gold
- HTTPS: 223 alive / 25 gold
- SOCKS4: 185 alive / 114 gold
- SOCKS5: 253 alive / 168 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
