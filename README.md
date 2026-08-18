# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 276
- HTTP: 403 alive / 25 gold
- HTTPS: 238 alive / 5 gold
- SOCKS4: 224 alive / 125 gold
- SOCKS5: 230 alive / 121 gold

## Historical pool

- Discovered: 102838
- Ever alive: 13085
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
