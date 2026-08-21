# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 396
- HTTP: 401 alive / 89 gold
- HTTPS: 204 alive / 20 gold
- SOCKS4: 216 alive / 141 gold
- SOCKS5: 222 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29743
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
