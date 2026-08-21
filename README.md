# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 390
- HTTP: 265 alive / 75 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 229 alive / 148 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29583
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
