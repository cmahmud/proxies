# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 441
- HTTP: 370 alive / 108 gold
- HTTPS: 260 alive / 35 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28382
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
