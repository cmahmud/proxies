# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 506
- HTTP: 390 alive / 151 gold
- HTTPS: 263 alive / 87 gold
- SOCKS4: 184 alive / 115 gold
- SOCKS5: 215 alive / 153 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17741
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
