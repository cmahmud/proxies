# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 401
- HTTP: 287 alive / 74 gold
- HTTPS: 210 alive / 14 gold
- SOCKS4: 273 alive / 153 gold
- SOCKS5: 267 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20585
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
