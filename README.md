# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 404
- HTTP: 301 alive / 96 gold
- HTTPS: 215 alive / 33 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 232 alive / 130 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30951
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
