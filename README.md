# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 423
- HTTP: 392 alive / 109 gold
- HTTPS: 282 alive / 28 gold
- SOCKS4: 222 alive / 156 gold
- SOCKS5: 238 alive / 130 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28447
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
