# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 523
- HTTP: 399 alive / 158 gold
- HTTPS: 260 alive / 91 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 207 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19893
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
