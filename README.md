# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 260
- HTTP: 246 alive / 30 gold
- HTTPS: 81 alive / 8 gold
- SOCKS4: 194 alive / 132 gold
- SOCKS5: 197 alive / 90 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9205
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
