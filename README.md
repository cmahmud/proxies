# SyndProxy private pool

## Current pool

- Alive now: 1137
- Gold now: 390
- HTTP: 366 alive / 88 gold
- HTTPS: 267 alive / 21 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 297 alive / 149 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22154
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
