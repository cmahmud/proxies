# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 513
- HTTP: 369 alive / 154 gold
- HTTPS: 265 alive / 86 gold
- SOCKS4: 188 alive / 133 gold
- SOCKS5: 202 alive / 140 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
