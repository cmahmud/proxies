# SyndProxy private pool

## Current pool

- Alive now: 1228
- Gold now: 404
- HTTP: 431 alive / 104 gold
- HTTPS: 298 alive / 25 gold
- SOCKS4: 208 alive / 129 gold
- SOCKS5: 291 alive / 146 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22572
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
