# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 260
- HTTP: 297 alive / 29 gold
- HTTPS: 156 alive / 3 gold
- SOCKS4: 214 alive / 118 gold
- SOCKS5: 226 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12064
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
