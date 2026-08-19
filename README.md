# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 357
- HTTP: 366 alive / 71 gold
- HTTPS: 243 alive / 12 gold
- SOCKS4: 214 alive / 129 gold
- SOCKS5: 246 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20357
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
