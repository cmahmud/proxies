# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 486
- HTTP: 368 alive / 126 gold
- HTTPS: 267 alive / 80 gold
- SOCKS4: 203 alive / 124 gold
- SOCKS5: 236 alive / 156 gold

## Historical pool

- Discovered: 119691
- Ever alive: 17864
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
