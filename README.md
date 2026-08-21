# SyndProxy private pool

## Current pool

- Alive now: 1204
- Gold now: 422
- HTTP: 448 alive / 109 gold
- HTTPS: 286 alive / 28 gold
- SOCKS4: 232 alive / 156 gold
- SOCKS5: 238 alive / 129 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28442
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
