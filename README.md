# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 439
- HTTP: 365 alive / 107 gold
- HTTPS: 257 alive / 29 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 265 alive / 164 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28429
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
