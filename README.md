# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 356
- HTTP: 339 alive / 53 gold
- HTTPS: 219 alive / 13 gold
- SOCKS4: 224 alive / 139 gold
- SOCKS5: 236 alive / 151 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14870
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
