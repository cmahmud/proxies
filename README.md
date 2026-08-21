# SyndProxy private pool

## Current pool

- Alive now: 1130
- Gold now: 420
- HTTP: 392 alive / 107 gold
- HTTPS: 290 alive / 28 gold
- SOCKS4: 218 alive / 156 gold
- SOCKS5: 230 alive / 129 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28447
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
