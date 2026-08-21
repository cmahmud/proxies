# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 418
- HTTP: 446 alive / 96 gold
- HTTPS: 304 alive / 25 gold
- SOCKS4: 228 alive / 139 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30419
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
