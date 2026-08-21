# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 404
- HTTP: 294 alive / 98 gold
- HTTPS: 227 alive / 24 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 240 alive / 146 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28254
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
