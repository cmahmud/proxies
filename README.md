# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 522
- HTTP: 374 alive / 156 gold
- HTTPS: 261 alive / 93 gold
- SOCKS4: 187 alive / 134 gold
- SOCKS5: 199 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19894
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
