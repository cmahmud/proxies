# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 348
- HTTP: 317 alive / 68 gold
- HTTPS: 194 alive / 13 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 202 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20240
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
