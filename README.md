# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 404
- HTTP: 316 alive / 102 gold
- HTTPS: 247 alive / 23 gold
- SOCKS4: 212 alive / 135 gold
- SOCKS5: 244 alive / 144 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28265
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
