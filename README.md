# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 522
- HTTP: 428 alive / 179 gold
- HTTPS: 267 alive / 98 gold
- SOCKS4: 198 alive / 116 gold
- SOCKS5: 192 alive / 129 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19405
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
