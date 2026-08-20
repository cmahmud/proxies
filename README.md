# SyndProxy private pool

## Current pool

- Alive now: 1568
- Gold now: 656
- HTTP: 595 alive / 251 gold
- HTTPS: 438 alive / 119 gold
- SOCKS4: 208 alive / 126 gold
- SOCKS5: 327 alive / 160 gold

## Historical pool

- Discovered: 143489
- Ever alive: 24808
- Ever gold: 1047

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
