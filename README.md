# SyndProxy private pool

## Current pool

- Alive now: 1200
- Gold now: 423
- HTTP: 399 alive / 89 gold
- HTTPS: 271 alive / 13 gold
- SOCKS4: 253 alive / 156 gold
- SOCKS5: 277 alive / 165 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20735
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
