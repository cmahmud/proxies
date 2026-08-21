# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 420
- HTTP: 407 alive / 109 gold
- HTTPS: 281 alive / 29 gold
- SOCKS4: 228 alive / 156 gold
- SOCKS5: 228 alive / 126 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28441
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
