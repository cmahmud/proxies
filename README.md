# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 521
- HTTP: 391 alive / 157 gold
- HTTPS: 259 alive / 91 gold
- SOCKS4: 203 alive / 134 gold
- SOCKS5: 205 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19893
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
