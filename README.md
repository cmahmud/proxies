# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 405
- HTTP: 297 alive / 94 gold
- HTTPS: 180 alive / 24 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 274 alive / 149 gold

## Historical pool

- Discovered: 154713
- Ever alive: 29004
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
