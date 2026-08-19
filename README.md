# SyndProxy private pool

## Current pool

- Alive now: 1269
- Gold now: 423
- HTTP: 429 alive / 89 gold
- HTTPS: 320 alive / 24 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 293 alive / 161 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22378
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
