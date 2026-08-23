# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 192
- HTTP: 139 alive / 39 gold
- HTTPS: 55 alive / 8 gold
- SOCKS4: 81 alive / 64 gold
- SOCKS5: 124 alive / 81 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32718
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
