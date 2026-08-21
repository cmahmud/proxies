# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 446
- HTTP: 406 alive / 108 gold
- HTTPS: 294 alive / 36 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 245 alive / 162 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28373
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
