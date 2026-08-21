# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 437
- HTTP: 364 alive / 104 gold
- HTTPS: 255 alive / 28 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 267 alive / 166 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28428
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
