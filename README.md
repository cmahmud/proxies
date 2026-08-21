# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 379
- HTTP: 347 alive / 91 gold
- HTTPS: 263 alive / 28 gold
- SOCKS4: 188 alive / 121 gold
- SOCKS5: 233 alive / 139 gold

## Historical pool

- Discovered: 153749
- Ever alive: 28827
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
