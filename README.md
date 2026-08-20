# SyndProxy private pool

## Current pool

- Alive now: 1235
- Gold now: 433
- HTTP: 401 alive / 102 gold
- HTTPS: 303 alive / 25 gold
- SOCKS4: 274 alive / 150 gold
- SOCKS5: 257 alive / 156 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25161
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
