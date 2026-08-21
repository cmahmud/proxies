# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 418
- HTTP: 327 alive / 106 gold
- HTTPS: 232 alive / 29 gold
- SOCKS4: 232 alive / 154 gold
- SOCKS5: 225 alive / 129 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30829
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
