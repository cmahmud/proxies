# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 347
- HTTP: 339 alive / 67 gold
- HTTPS: 190 alive / 13 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 203 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20240
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
